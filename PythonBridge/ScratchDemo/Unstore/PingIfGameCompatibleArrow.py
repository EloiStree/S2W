
import socket
import struct
import time


# --------------- VARIABLES ---------------

target_ip ="127.0.0.1"
target_port = 7073
player_id_targeted = 0


key_left = 1037
key_right = 1039
key_up = 1038
key_down = 1040


key_alpha_0 = 1048
key_alpha_1 = 1049
key_alpha_2 = 1050
key_alpha_3 = 1051

key_space = 1032

key_tab = 1009
key_enter = 1013

use_key_tab = False
use_key_enter = False
use_key_space = False
use_key_alpha = False


time_between_key_test =1
time_between_press =1



# --------------- FUNCTIONS ---------------


def send_index_integer_command_with_ip(ip_of_computer, port_of_application, id_player, id_key):
    message = struct.pack('<iiq', id_player, id_key, 0) # 1010101110101....00111101100
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (ip_of_computer, port_of_application))
    sock.close()


def press_release_key(key):
    print("Pressing key: " + str(key))
    send_index_integer_command_with_ip(target_ip, target_port, player_id_targeted, key)
    time.sleep(time_between_press)  # Simulate key press duration
    print("Releasing key: " + str(key))
    send_index_integer_command_with_ip(target_ip, target_port, player_id_targeted, key + 1000)  # Release key

def wait_a_bit():
    time.sleep(time_between_key_test)



# --------------- MAIN LOOP ---------------

while True:
    press_release_key(key_left)
    wait_a_bit()
    press_release_key(key_right)
    wait_a_bit()
    press_release_key(key_up)
    wait_a_bit()
    press_release_key(key_down)
    wait_a_bit()

    if use_key_alpha:
        press_release_key(key_alpha_0)
        wait_a_bit()
        press_release_key(key_alpha_1)
        wait_a_bit()
        press_release_key(key_alpha_2)
        wait_a_bit()
        press_release_key(key_alpha_3)
        wait_a_bit()
        
    if use_key_space:
        press_release_key(key_space)
        wait_a_bit()
    if use_key_tab:
        press_release_key(key_tab)
        wait_a_bit()
    if use_key_enter:
        press_release_key(key_enter)
        wait_a_bit()
      



