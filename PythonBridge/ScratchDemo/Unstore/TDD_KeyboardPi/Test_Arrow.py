# pip install iid42
import iid42 , time
import wowint
from wowint import WowIntegerKeyboard

from iid42 import SendUdpIID
# Send IID to a UDP Gate Relay
# Replace 127.0.0.1 with the computer you want to target or the game server
# Example: 192.168.1.42  http://apint.ddns.net 
target = SendUdpIID("192.168.1.113",7073,True)
# Send the action 42 to the target with UDP to 127.0.0.1 computer on the applicaton behind 3615 port.

def press_and_release_key_1000(key, timing):

    time.sleep(timing)
    target.push_integer(key)
    time.sleep(timing)
    target.push_integer(key+1000)

def press_and_release_1000(key, timing):

    time.sleep(timing)
    target.push_integer(key+1000)
    time.sleep(timing)
    target.push_integer(key+2000)


for i in range(1):
    press_and_release_key_1000(WowIntegerKeyboard.arrow_up,1) # Up Arrow
    press_and_release_key_1000(WowIntegerKeyboard.arrow_down,1) # Down Arrow
    press_and_release_key_1000(WowIntegerKeyboard.arrow_left,1) # Left Arrow
    press_and_release_key_1000(WowIntegerKeyboard.arrow_right,1) # Right Arrow

    press_and_release_key_1000(WowIntegerKeyboard.numpad_add,1) # Numpad Add Key
    press_and_release_key_1000(WowIntegerKeyboard.numpad_subtract,1) # Numpad Subtract Key
    press_and_release_key_1000(WowIntegerKeyboard.numpad_multiply,1) # Numpad Multiply Key
    press_and_release_key_1000(WowIntegerKeyboard.numpad_divide,1) # Numpad Divide Key
    press_and_release_key_1000(WowIntegerKeyboard.numpad_decimal,1) # Numpad Decimal Key

    press_and_release_key_1000(WowIntegerKeyboard.escape,1) # Escape Key

    press_and_release_key_1000(WowIntegerKeyboard.oem_1,1) # OEM 1 Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_plus,1) # OEM Plus Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_comma,1) # OEM Comma Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_minus,1) # OEM Minus Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_period,1) # OEM Period Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_2,1) # OEM 2 Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_3,1) # OEM 3 Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_4,1) # OEM 4 Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_5,1) # OEM 5 Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_6,1) # OEM 6 Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_7,1) # OEM 7 Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_8,1) # OEM 8 Key
    press_and_release_key_1000(WowIntegerKeyboard.oem_102,1) # OEM 102 Key



    # Press and release keys 'a' to 'z'
    for key_code in range(65, 91):  # ASCII codes for 'A' to 'Z'
        press_and_release_key_1000(key_code, 0.1)

    press_and_release_key_1000(WowIntegerKeyboard.numpad_0, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.numpad_1, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.numpad_2, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.numpad_3, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.numpad_4, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.numpad_5, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.numpad_6, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.numpad_7, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.numpad_8, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.numpad_9, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_0, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_1, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_2, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_3, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_4, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_5, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_6, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_7, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_8, 0.1)
    press_and_release_key_1000(WowIntegerKeyboard.alpha_9, 0.1)




    # press and release tab
    press_and_release_key_1000(WowIntegerKeyboard.tab,1) # Tab Key
    # press and release caps lock
    press_and_release_key_1000(WowIntegerKeyboard.caps_lock,1) # Caps Lock Key
    # press and release shift left
    press_and_release_key_1000(WowIntegerKeyboard.left_shift,1) # Shift Key
    # press and release ctrl left
    press_and_release_key_1000(WowIntegerKeyboard.left_control,1) # Ctrl Key
    # press and release alt left
    press_and_release_key_1000(WowIntegerKeyboard.left_alt,1) # Alt Key
    # press and release space
    press_and_release_key_1000(WowIntegerKeyboard.space,1) # Space Key
    # press and release alt right
    press_and_release_key_1000(WowIntegerKeyboard.right_alt,1) # Alt Key
    # press and release ctrl right
    press_and_release_key_1000(WowIntegerKeyboard.right_control,1) # Ctrl Key
    # press and release shift right
    press_and_release_key_1000(WowIntegerKeyboard.right_shift,1) # Shift Key
    # press and release enter
    press_and_release_key_1000(WowIntegerKeyboard.enter,1) # Enter Key
    # press and release backspace
    press_and_release_key_1000(WowIntegerKeyboard.backspace,1) # Backspace Key
    # press and release delete
    press_and_release_key_1000(WowIntegerKeyboard.delete,1) # Delete Key
    # press and release insert
    press_and_release_key_1000(WowIntegerKeyboard.insert,1) # Insert Key
    # press and release home
    press_and_release_key_1000(WowIntegerKeyboard.home,1) # Home Key
    # press and release end
    press_and_release_key_1000(WowIntegerKeyboard.end,1) # End Key
    # press and release page up
    press_and_release_key_1000(WowIntegerKeyboard.page_up,1) # Page Up Key
    # press and release page down
    press_and_release_key_1000(WowIntegerKeyboard.page_down,1) # Page Down Key

    

    press_and_release_key_1000(WowIntegerKeyboard.f1,1) # F1 Key
    press_and_release_key_1000(WowIntegerKeyboard.f2,1) # F2 Key
    press_and_release_key_1000(WowIntegerKeyboard.f3,1) # F3 Key
    press_and_release_key_1000(WowIntegerKeyboard.f4,1) # F4 Key
    press_and_release_key_1000(WowIntegerKeyboard.f5,1) # F5 Key
    press_and_release_key_1000(WowIntegerKeyboard.f6,1) # F6 Key
    press_and_release_key_1000(WowIntegerKeyboard.f7,1) # F7 Key
    press_and_release_key_1000(WowIntegerKeyboard.f8,1) # F8 Key
    press_and_release_key_1000(WowIntegerKeyboard.f9,1) # F9 Key
    press_and_release_key_1000(WowIntegerKeyboard.f10,1) # F10 Key
    press_and_release_key_1000(WowIntegerKeyboard.f11,1) # F11 Key
    press_and_release_key_1000(WowIntegerKeyboard.f12,1) # F12 Key
