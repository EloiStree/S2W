// ==UserScript==
// @name         Push Scratch wsvar to Local WebSocket
// @namespace    http://tampermonkey.net/
// @version      0.3.0
// @description  Sends Scratch variables named "wsvar ..." to a local WebSocket server.
// @author       Eloi Stree
// @match        https://scratch.mit.edu/projects/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=scratch.mit.edu
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    /*
     * ============================================================
     * Configuration
     * ============================================================
     */

    const SOCKET_URL = 'ws://localhost:7072';

    const SCAN_INTERVAL_MS = 100;

    const RECONNECT_DELAY_MS = 1000;
    const MAX_RECONNECT_DELAY_MS = 10000;

    // Keep this TRUE while testing.
    const DEBUG = true;


    /*
     * ============================================================
     * State
     * ============================================================
     */

    let socket = null;
    let reconnectTimer = null;
    let reconnectDelay = RECONNECT_DELAY_MS;

    // Last value successfully sent for each wsvar.
    const previousData = new Map();


    /*
     * ============================================================
     * Logging
     * ============================================================
     */

    function debugLog(...args) {
        if (DEBUG) {
            console.log('[Scratch WS]', ...args);
        }
    }


    /*
     * ============================================================
     * WebSocket
     * ============================================================
     */

    function isSocketOpen() {
        return socket !== null &&
               socket.readyState === WebSocket.OPEN;
    }


    function connectWebSocket() {

        if (
            socket &&
            (
                socket.readyState === WebSocket.OPEN ||
                socket.readyState === WebSocket.CONNECTING
            )
        ) {
            return;
        }

        clearReconnectTimer();

        console.log(
            '[Scratch WS] Connecting to:',
            SOCKET_URL
        );

        try {

            const ws = new WebSocket(SOCKET_URL);

            ws.binaryType = 'arraybuffer';

            socket = ws;


            ws.addEventListener('open', () => {

                if (socket !== ws) {
                    return;
                }

                reconnectDelay = RECONNECT_DELAY_MS;

                console.log(
                    '[Scratch WS] Connected:',
                    SOCKET_URL
                );

            });


            ws.addEventListener('message', (event) => {

                debugLog(
                    'Received from server:',
                    event.data
                );

            });


            ws.addEventListener('error', (error) => {

                console.error(
                    '[Scratch WS] WebSocket error:',
                    error
                );

            });


            ws.addEventListener('close', (event) => {

                if (socket !== ws) {
                    return;
                }

                socket = null;

                console.log(
                    '[Scratch WS] Connection closed.',
                    `code=${event.code}`
                );

                scheduleReconnect();

            });

        } catch (error) {

            console.error(
                '[Scratch WS] Failed to create WebSocket:',
                error
            );

            socket = null;

            scheduleReconnect();
        }
    }


    function scheduleReconnect() {

        if (reconnectTimer !== null) {
            return;
        }

        const delay = reconnectDelay;

        debugLog(
            `Reconnect scheduled in ${delay} ms`
        );

        reconnectTimer = setTimeout(() => {

            reconnectTimer = null;

            connectWebSocket();

            reconnectDelay = Math.min(
                reconnectDelay * 2,
                MAX_RECONNECT_DELAY_MS
            );

        }, delay);
    }


    function clearReconnectTimer() {

        if (reconnectTimer !== null) {

            clearTimeout(reconnectTimer);

            reconnectTimer = null;
        }
    }


    /*
     * ============================================================
     * Send uint32
     * ============================================================
     */

    function sendUint32(value) {

        if (!isSocketOpen()) {

            debugLog(
                'Cannot send because WebSocket is not open.'
            );

            return false;
        }

        const number = Number(value);

        if (!Number.isInteger(number)) {

            console.warn(
                '[Scratch WS] Not an integer:',
                value
            );

            return false;
        }

        if (
            number < 0 ||
            number > 0xFFFFFFFF
        ) {

            console.warn(
                '[Scratch WS] Value outside uint32 range:',
                number
            );

            return false;
        }


        const buffer = new ArrayBuffer(4);

        const view = new DataView(buffer);

        // uint32 little-endian
        view.setUint32(
            0,
            number,
            true
        );


        try {

            socket.send(buffer);

            console.log(
                '[Scratch WS] Sent:',
                number
            );

            return true;

        } catch (error) {

            console.error(
                '[Scratch WS] Send failed:',
                error
            );

            return false;
        }
    }


    /*
     * ============================================================
     * Scratch variable detection
     * ============================================================
     *
     * Scratch's monitor CSS class names can change.
     *
     * Instead of depending on:
     *
     * .react-contextmenu-wrapper
     *
     * monitor_label_xxx
     * monitor_value_xxx
     *
     * we inspect elements containing the monitor text.
     * ============================================================
     */

  function extractAndSendData() {

    /*
     * Find every DIV on the page.
     */
    const divs = document.querySelectorAll('div');

    for (const div of divs) {

        /*
         * Look for "wsvar" in this DIV.
         *
         * We only use this DIV as the container.
         */
        const labelElement = div.querySelector(
            '[class^="monitor_label_"]'
        );

        if (!labelElement) {
            continue;
        }

        const label = labelElement.textContent.trim();

        if (!label.toLowerCase().startsWith('wsvar ')) {
            continue;
        }

        /*
         * We found the DIV containing the wsvar.
         *
         * Now find the monitor VALUE INSIDE THIS DIV.
         */
        const valueElement = div.querySelector(
            '[class^="monitor_value_"]'
        );

        if (!valueElement) {
            debugLog(
                'Found wsvar but no monitor value:',
                label,
                div
            );

            continue;
        }

        /*
         * Extract ONLY the value.
         */
        const valueText = valueElement.textContent.trim();

        debugLog(
            'wsvar:',
            label,
            'value:',
            valueText
        );

        /*
         * Scratch can sometimes put extra whitespace in
         * the value, so normalize it.
         */
        const value = valueText.replace(/\s+/g, '');

        /*
         * We only accept unsigned integers because the
         * WebSocket protocol is uint32.
         */
        if (!/^\d+$/.test(value)) {

            debugLog(
                'Ignoring non-integer value:',
                valueText
            );

            continue;
        }

        /*
         * Convert the VALUE to a JavaScript number.
         *
         * The variable name is NOT sent.
         */
        const number = Number(value);

        if (
            !Number.isSafeInteger(number) ||
            number < 0 ||
            number > 0xFFFFFFFF
        ) {

            console.warn(
                '[Scratch WS] Invalid uint32 value:',
                number
            );

            continue;
        }

        /*
         * Only send when the VALUE changes.
         */
        const previousValue = previousData.get(label);

        if (previousValue === number) {
            continue;
        }

        /*
         * Send ONLY the numeric value.
         */
        if (!sendUint32(number)) {

            debugLog(
                'Could not send value:',
                number
            );

            continue;
        }

        /*
         * Remember what was successfully sent.
         */
        previousData.set(label, number);

        console.log(
            '[Scratch WS] Sent wsvar value:',
            number
        );
    }
}


    /*
     * ============================================================
     * Startup
     * ============================================================
     */

    console.log(
        '[Scratch WS] Script loaded.'
    );

    console.log(
        '[Scratch WS] WebSocket:',
        SOCKET_URL
    );


    connectWebSocket();


    /*
     * Scan Scratch regularly.
     */

    setInterval(
        extractAndSendData,
        SCAN_INTERVAL_MS
    );


})();
