# pip install pyperclip pyautogui pynput --break-system-packages
import time
import socket
import pyperclip
import psutil
import asyncio
import threading
from pynput.mouse import Button, Controller
import pyautogui
from pynput.keyboard import Key, Controller as KeyboardController

lisent_udp_port_to_interact = 7073
debug_at_pression_send=True
use_print_log=False
use_print_log=True




def get_local_ips():
    local_ips = []
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == socket.AF_INET:
                local_ips.append(snic.address)
    return local_ips

local_ips = get_local_ips()
print(f"Local IPs: {local_ips}")
            


######################### NE PAS TOUCHER ############################
######################### DONT TOUCH ############################


# Constants for SendMessage
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101


keyboard = KeyboardController()

def press_key(hexKeyCode):
    key_found = key_map.try_to_guess_key(hexKeyCode)

    if not key_found:  # nothing found
        print(f"[NOT FOUND] No key mapping for hex {hex(hexKeyCode)}")
        return

    key = key_found[0]
    print("PRESS", key.name)

    try:
        if key.pynput is not None:
            keyboard.press(key.pynput)
        elif key.pyautogui is not None:
            pyautogui.keyDown(key.pyautogui)
        else:
            print(f"[NO HANDLER] {key.name} has no pynput/pyautogui mapping")
    except Exception as e:
        print(f"[WARN] press_key failed for {key.name}: {e}")


def release_key(hexKeyCode):
    key_found = key_map.try_to_guess_key(hexKeyCode)

    if not key_found:  # nothing found
        print(f"[NOT FOUND] No key mapping for hex {hex(hexKeyCode)}")
        return

    key = key_found[0]
    print("RELEASE", key.name)

    try:
        if key.pynput is not None:
            keyboard.release(key.pynput)
        elif key.pyautogui is not None:
            pyautogui.keyUp(key.pyautogui)
        else:
            print(f"[NO HANDLER] {key.name} has no pynput/pyautogui mapping")
    except Exception as e:
        print(f"[WARN] release_key failed for {key.name}: {e}")
        pass  # Ignore if not a printable character


timebetweenaction=0.1
timepress=0.1




def check_and_copy(message):
    if message.startswith("c "):
        content = message[2:]  # Extract the content after "c "
        pyperclip.copy(content)
        if use_print_log:
            print("Content copied to clipboard:", content)
        return True
    else:
        return False


mouse = Controller()
screen_size=pyautogui.size()

def move_mouse_with_integer(int_value):
    
    float_x:float = (int_value/10000 % 10000)/9999.0
    float_y:float = (int_value % 10000)/9999.0
    
    screen_size=pyautogui.size()
    mouse.position = (screen_size[0]*float_x,screen_size[1]*(1.0-float_y))
    
    if use_print_log:
        print(f"Move mouse to {screen_size[0]*float_x} {screen_size[1]*(1.0-float_y)}")
    
    

def push_to_index_integer(int_index, int_value):
    global keyboard_mappings
    
    
    
    #print("start")
    if use_print_log:
        print(f"R | Index {int_index}| Value {int_value}")

    int_value_tag = int(int_value/100000000)
    
    if use_print_log:
        print("Tag",int_value_tag)
    if int_value_tag==15:
        move_mouse_with_integer(int_value)
        return
    if int_value== 1260:
        mouse.press(Button.left)
        return
        
    elif int_value== 2260:
        mouse.release(Button.left)
        return
    elif int_value== 1261:
        mouse.press(Button.middle)
        return
    elif int_value== 2261:
        mouse.release(Button.middle)
        return
    elif int_value== 1262:
        mouse.press(Button.right)
        return
    elif int_value== 2262:
        mouse.release(Button.right)
        return
    elif int_value== 1263:
        mouse.press(Button.x1)
        return
    elif int_value== 2263:
        mouse.release(Button.x1)
        return
    elif int_value== 1264:
        mouse.press(Button.x2)
        return
    elif int_value== 2264:
        mouse.release(Button.x2)
        return
        
    
    key_name_last_found=""
    press_last_found=False
    one_found=False



    key_info = key_map.try_to_guess_key(str(int_value))
    if key_info is None or key_info[0] is None:
        return
        
    
    if use_print_log:
        
        print(f"Push {int_value} to Window {int_index} ({key_info[0].name} / {key_info[0].hexadecimal})")
        print(f"Push {key_info[0]}")
    ## If the value is existing in the mapping allows to player
    int_value_as_string = str(int_value)
    
    
    if use_print_log:
        print (f"{int_value}  {key_info[1]}   {key_info[2]}")
    
    if key_info[1]:
        press_key(int(key_info[0].decimal))
        
    if key_info[2]:
        release_key(int(key_info[0].decimal))
   


async def async_task():
        
        print("Async task started")
        await asyncio.sleep(2)
        print("Async task ready")
        
        # Launch the async task

        for key in list(keyboard_mappings.keys()):
            keyboard_mappings[key.lower().replace(" ", "")] = keyboard_mappings.pop(key)

        # Define the UDP IP address and port to listen on
        UDP_IP = "127.0.0.1"  # PC LOCAL ON LY 
        UDP_IP = "0.0.0.0" # ANY ONE
        

        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind the socket to the port
        sock.bind((UDP_IP, lisent_udp_port_to_interact))


        print("UDP server listening on port", lisent_udp_port_to_interact)

        try:
            while True:
                data, addr = sock.recvfrom(1024)  
                
                byte_counter = len(data)
                #print("received message:", data)  
                
                if use_print_log:
                    print(f"R| {len(data)} | {data}")
                if byte_counter == 4:
                    int_value = int.from_bytes(data, byteorder='little')
                    if use_print_log:
                        print(f"Value {int_value} ")
                    push_to_index_integer(0,int_value)
                if byte_counter == 8:
                    int_index = int.from_bytes(data[0:4], byteorder='little')
                    int_value = int.from_bytes(data[4:8], byteorder='little')
                    if use_print_log:
                        print(f"Index {int_index} | Value {int_value}")
                    push_to_index_integer(int_index, int_value)
                    
                elif  byte_counter==12:

                    int_value= int.from_bytes(data[0:4], byteorder='little')
                    long_data_2= int.from_bytes(data[4:12], byteorder='little')
                    push_to_index_integer(0,int_value)
                    if use_print_log:
                        print("Value ",int_value)
                        
                elif  byte_counter==16:

                    int_index= int.from_bytes(data[0:4], byteorder='little')
                    int_value= int.from_bytes(data[4:8], byteorder='little')
                    long_data_2= int.from_bytes(data[8:16], byteorder='little')
                    if use_print_log :
                        print("Index ",int_index,"Value",int_value)
                    push_to_index_integer(int_index, int_value)
                    # thread = threading.Thread(target=push_to_index_integer, args=(int_index, int_value))
                    # thread.start()
        except KeyboardInterrupt:
            print("Server stopped.")
        
from pynput.keyboard import Key

class KeyInfo:
    def __init__(self, name, decimal, hexadecimal, press, release, pynput_key=None, pyautogui_key=None):
        self.name = name
        self.decimal = decimal
        self.hexadecimal = hexadecimal
        self.press = press
        self.release = release
        self.pynput = pynput_key
        self.pyautogui = pyautogui_key
        
    def __repr__(self):
        return (f"KeyInfo(name='{self.name}', decimal={self.decimal}, "
                f"hexadecimal='{self.hexadecimal}', press={self.press}, release={self.release}, "
                f"pynput={self.pynput}, pyautogui={self.pyautogui})")


class KeyMap:
    def __init__(self):
        self.keys = {
            # Control keys
            "Backspace": KeyInfo("Backspace", 8, 0x08, 1008, 2008, Key.backspace, "backspace"),
            "Tab": KeyInfo("Tab", 9, 0x09, 1009, 2009, Key.tab, "tab"),
            "Clear": KeyInfo("Clear", 12, 0x0C, 1012, 2012, None, None),
            "Enter": KeyInfo("Enter", 13, 0x0D, 1013, 2013, Key.enter, "enter"),
            "Shift": KeyInfo("Shift", 16, 0x10, 1016, 2016, Key.shift, "shift"),
            "Ctrl": KeyInfo("Ctrl", 17, 0x11, 1017, 2017, Key.ctrl, "ctrl"),
            "Alt": KeyInfo("Alt", 18, 0x12, 1018, 2018, Key.alt, "alt"),
            "Pause": KeyInfo("Pause", 19, 0x13, 1019, 2019, Key.pause, None),
            "CapsLock": KeyInfo("CapsLock", 20, 0x14, 1020, 2020, Key.caps_lock, "capslock"),
            "Esc": KeyInfo("Esc", 27, 0x1B, 1027, 2027, Key.esc, "esc"),
            "Escape": KeyInfo("Escape", 27, 0x1B, 1027, 2027, Key.esc, "esc"),
            "Space": KeyInfo("Space", 32, 0x20, 1032, 2032, Key.space, "space"),
            "PageUp": KeyInfo("PageUp", 33, 0x21, 1033, 2033, Key.page_up, "pageup"),
            "PageDown": KeyInfo("PageDown", 34, 0x22, 1034, 2034, Key.page_down, "pagedown"),
            "End": KeyInfo("End", 35, 0x23, 1035, 2035, Key.end, "end"),
            "Home": KeyInfo("Home", 36, 0x24, 1036, 2036, Key.home, "home"),
            "LeftArrow": KeyInfo("LeftArrow", 37, 0x25, 1037, 2037, Key.left, "left"),
            "Left": KeyInfo("Left", 37, 0x25, 1037, 2037, Key.left, "left"),
            "UpArrow": KeyInfo("UpArrow", 38, 0x26, 1038, 2038, Key.up, "up"),
            "Up": KeyInfo("Up", 38, 0x26, 1038, 2038, Key.up, "up"),
            "RightArrow": KeyInfo("RightArrow", 39, 0x27, 1039, 2039, Key.right, "right"),
            "Right": KeyInfo("Right", 39, 0x27, 1039, 2039, Key.right, "right"),
            "DownArrow": KeyInfo("DownArrow", 40, 0x28, 1040, 2040, Key.down, "down"),
            "Down": KeyInfo("Down", 40, 0x28, 1040, 2040, Key.down, "down"),
            "Select": KeyInfo("Select", 41, 0x29, 1041, 2041, None, None),
            "Print": KeyInfo("Print", 42, 0x2A, 1042, 2042, None, None),
            "Execute": KeyInfo("Execute", 43, 0x2B, 1043, 2043, None, None),
            "PrintScreen": KeyInfo("PrintScreen", 44, 0x2C, 1044, 2044, Key.print_screen, "printscreen"),
            "Insert": KeyInfo("Insert", 45, 0x2D, 1045, 2045, Key.insert, "insert"),
            "Delete": KeyInfo("Delete", 46, 0x2E, 1046, 2046, Key.delete, "delete"),

            # Numbers
            **{str(n): KeyInfo(str(n), 48+n, hex(48+n), 1048+n, 2048+n, str(n), str(n)) for n in range(10)},

            # Letters
            **{ch: KeyInfo(ch, ord(ch), hex(ord(ch)), 1000+ord(ch), 2000+ord(ch), ch.lower(), ch.lower())
               for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"},

            # Windows keys
            "LeftWindows": KeyInfo("LeftWindows", 91, 0x5B, 1091, 2091, Key.cmd, "win"),
            "RightWindows": KeyInfo("RightWindows", 92, 0x5C, 1092, 2092, Key.cmd_r, None),
            "Applications": KeyInfo("Applications", 93, 0x5D, 1093, 2093, None, None),
            "Sleep": KeyInfo("Sleep", 95, 0x5F, 1095, 2095, None, None),

            # Numpad
            "Numpad0": KeyInfo("Numpad0", 96, 0x60, 1096, 2096, None, "num0"),
            "Numpad1": KeyInfo("Numpad1", 97, 0x61, 1097, 2097, None, "num1"),
            "Numpad2": KeyInfo("Numpad2", 98, 0x62, 1098, 2098, None, "num2"),
            "Numpad3": KeyInfo("Numpad3", 99, 0x63, 1099, 2099, None, "num3"),
            "Numpad4": KeyInfo("Numpad4", 100, 0x64, 1100, 2100, None, "num4"),
            "Numpad5": KeyInfo("Numpad5", 101, 0x65, 1101, 2101, None, "num5"),
            "Numpad6": KeyInfo("Numpad6", 102, 0x66, 1102, 2102, None, "num6"),
            "Numpad7": KeyInfo("Numpad7", 103, 0x67, 1103, 2103, None, "num7"),
            "Numpad8": KeyInfo("Numpad8", 104, 0x68, 1104, 2104, None, "num8"),
            "Numpad9": KeyInfo("Numpad9", 105, 0x69, 1105, 2105, None, "num9"),
            "Multiply": KeyInfo("Multiply", 106, 0x6A, 1106, 2106, None, "multiply"),
            "Add": KeyInfo("Add", 107, 0x6B, 1107, 2107, None, "add"),
            "Separator": KeyInfo("Separator", 108, 0x6C, 1108, 2108, None, None),
            "Subtract": KeyInfo("Subtract", 109, 0x6D, 1109, 2109, None, "subtract"),
            "Decimal": KeyInfo("Decimal", 110, 0x6E, 1110, 2110, None, "decimal"),
            "Divide": KeyInfo("Divide", 111, 0x6F, 1111, 2111, None, "divide"),

            # Function keys F1–F24
            **{f"F{i}": KeyInfo(f"F{i}", 111+i, hex(111+i), 1111+i, 2111+i,
                                getattr(Key, f"f{i}") if hasattr(Key, f"f{i}") else None,
                                f"f{i}") for i in range(1, 25)},

            # Lock keys
            "NumLock": KeyInfo("NumLock", 144, 0x90, 1144, 2144, Key.num_lock, "numlock"),
            "ScrollLock": KeyInfo("ScrollLock", 145, 0x91, 1145, 2145, Key.scroll_lock, "scrolllock"),

            # Shift/Ctrl variants
            "LeftShift": KeyInfo("LeftShift", 160, 0xA0, 1160, 2160, Key.shift_l, None),
            "RightShift": KeyInfo("RightShift", 161, 0xA1, 1161, 2161, Key.shift_r, None),
            "LeftCtrl": KeyInfo("LeftCtrl", 162, 0xA2, 1162, 2162, Key.ctrl_l, None),
            "RightCtrl": KeyInfo("RightCtrl", 163, 0xA3, 1163, 2163, Key.ctrl_r, None),
            "LeftMenu": KeyInfo("LeftMenu", 164, 0xA4, 1164, 2164, None, None),
            "RightMenu": KeyInfo("RightMenu", 165, 0xA5, 1165, 2165, None, None),

            # Browser/media/launch (not in PyAutoGUI, partial in pynput)
            "BrowserBack": KeyInfo("BrowserBack", 166, 0xA6, 1166, 2166, None, None),
            "BrowserForward": KeyInfo("BrowserForward", 167, 0xA7, 1167, 2167, None, None),
            "BrowserRefresh": KeyInfo("BrowserRefresh", 168, 0xA8, 1168, 2168, None, None),
            "BrowserStop": KeyInfo("BrowserStop", 169, 0xA9, 1169, 2169, None, None),
            "BrowserSearch": KeyInfo("BrowserSearch", 170, 0xAA, 1170, 2170, None, None),
            "BrowserFavorites": KeyInfo("BrowserFavorites", 171, 0xAB, 1171, 2171, None, None),
            "BrowserHome": KeyInfo("BrowserHome", 172, 0xAC, 1172, 2172, None, None),
            "VolumeMute": KeyInfo("VolumeMute", 173, 0xAD, 1173, 2173, None, None),
            "VolumeDown": KeyInfo("VolumeDown", 174, 0xAE, 1174, 2174, None, None),
            "VolumeUp": KeyInfo("VolumeUp", 175, 0xAF, 1175, 2175, None, None),
            "MediaNextTrack": KeyInfo("MediaNextTrack", 176, 0xB0, 1176, 2176, None, None),
            "MediaPrevTrack": KeyInfo("MediaPrevTrack", 177, 0xB1, 1177, 2177, None, None),
            "MediaStop": KeyInfo("MediaStop", 178, 0xB2, 1178, 2178, None, None),
            "MediaPlayPause": KeyInfo("MediaPlayPause", 179, 0xB3, 1179, 2179, None, None),
            "LaunchMail": KeyInfo("LaunchMail", 180, 0xB4, 1180, 2180, None, None),
            "LaunchMediaSelect": KeyInfo("LaunchMediaSelect", 181, 0xB5, 1181, 2181, None, None),
            "LaunchApp1": KeyInfo("LaunchApp1", 182, 0xB6, 1182, 2182, None, None),
            "LaunchApp2": KeyInfo("LaunchApp2", 183, 0xB7, 1183, 2183, None, None),
        }


    def get_key_info(self, key_name):
        return self.keys.get(key_name, None)
    
    def find_key_in_press(self, press):
        for key_info in self.keys.values():
            if key_info.press == press:
                return key_info
        return None
    
    def find_key_in_release(self, release):
        for key_info in self.keys.values():
            if key_info.release == release:
                return key_info
        return None
    
    def find_key_in_decimal(self, decimal):
        for key_info in self.keys.values():
            if key_info.decimal == decimal:
                return key_info
        return None
    
    def find_key_in_hexadecimal(self, hexadecimal):
        for key_info in self.keys.values():
            if key_info.hexadecimal == hexadecimal:
                return key_info
        return None
    
    def find_key_in_name(self, name):
        for key_info in self.keys.values():
            if key_info.name == name:
                return key_info
        return None
    
    def find_key_in_name_lower(self, name):
        name = name.lower()
        for key_info in self.keys.values():
            if key_info.name.lower() == name:
                return key_info
        return None
    
    def try_to_guess_key(self, key):
       
        key = str(key)

        key= key.lower().replace(" ", "")
        key_info = self.find_key_in_press(key)
        if(key_info is not None):
            return key_info, True, False
        
        key_info = self.find_key_in_release(key)
        if(key_info is not None):
            return key_info, False , True
        
        
        key_info = self.find_key_in_hexadecimal(key)
        if(key_info is not None):
            return key_info,True, True
        
        
        key_info = self.find_key_in_decimal(key)
        if(key_info is not None):
            return key_info,True, True
        
        key_info = self.find_key_in_name(key)
        if(key_info is not None):
            return key_info,True, True
        
        key_info = self.find_key_in_name_lower(key)
        if(key_info is not None):
            return key_info,True, True

key_map = KeyMap()


def remove_spaces(text: str) -> str:
    return str(text.replace(" ", "").lower())

for key_info in key_map.keys:
    key_map.keys[key_info].name = remove_spaces(str(key_map.keys[key_info].name))
    key_map.keys[key_info].press = remove_spaces(str(key_map.keys[key_info].press))
    key_map.keys[key_info].release = remove_spaces(str(key_map.keys[key_info].release))
    key_map.keys[key_info].hexadecimal = remove_spaces(str(key_map.keys[key_info].hexadecimal))
    key_map.keys[key_info].decimal = remove_spaces(str(key_map.keys[key_info].decimal))
    
key_info= key_map.get_key_info("Enter")
print("ID",key_info)

key_info = key_map.try_to_guess_key("1013")
print("Press",key_info)

key_info = key_map.try_to_guess_key("2013")
print("Release",key_info)

key_info = key_map.try_to_guess_key("0x0D")
print("Decimal",key_info)

key_info = key_map.try_to_guess_key("13")
print("Integer",key_info)

key_info = key_map.try_to_guess_key("Enter")
print("Name case",key_info)

key_info = key_map.try_to_guess_key("enter")
print("Name no case",key_info)


    

if __name__ == "__main__":
   
    keyboard_mappings = {
    "Backspace": 0x08,
    "Tab": 0x09,
    "Clear": 0x0C,
    "Enter": 0x0D,
    "Shift": 0x10,
    "Ctrl": 0x11,
    "Alt": 0x12,
    "Pause": 0x13,
    "CapsLock": 0x14,
    "Esc": 0x1B,
    "Escape": 0x1B,
    "Space": 0x20,
    "PageUp": 0x21,
    "PageDown": 0x22,
    "End": 0x23,
    "Home": 0x24,
    "LeftArrow": 0x25,
    "Left": 0x25,
    "UpArrow": 0x26,
    "Up": 0x26,
    "RightArrow": 0x27,
    "Right": 0x27,
    "DownArrow": 0x28,
    "Down": 0x28,
    "Select": 0x29,
    "Print": 0x2A,
    "Execute": 0x2B,
    "PrintScreen": 0x2C,
    "Insert": 0x2D,
    "Delete": 0x2E,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'A': 0x41,
    'B': 0x42,
    'C': 0x43,
    'D': 0x44,
    'E': 0x45,
    'F': 0x46,
    'G': 0x47,
    'H': 0x48,
    'I': 0x49,
    'J': 0x4A,
    'K': 0x4B,
    'L': 0x4C,
    'M': 0x4D,
    'N': 0x4E,
    'O': 0x4F,
    'P': 0x50,
    'Q': 0x51,
    'R': 0x52,
    'S': 0x53,
    'T': 0x54,
    'U': 0x55,
    'V': 0x56,
    'W': 0x57,
    'X': 0x58,
    'Y': 0x59,
    'Z': 0x5A,
    "LeftWindows": 0x5B,
    "RightWindows": 0x5C,
    "Applications": 0x5D,
    "Sleep": 0x5F,
    "Numpad0": 0x60,
    "Numpad1": 0x61,
    "Numpad2": 0x62,
    "Numpad3": 0x63,
    "Numpad4": 0x64,
    "Numpad5": 0x65,
    "Numpad6": 0x66,
    "Numpad7": 0x67,
    "Numpad8": 0x68,
    "Numpad9": 0x69,
    "Multiply": 0x6A,
    "NP0": 0x60,
    "NP1": 0x61,
    "NP2": 0x62,
    "NP3": 0x63,
    "NP4": 0x64,
    "NP5": 0x65,
    "NP6": 0x66,
    "NP7": 0x67,
    "NP8": 0x68,
    "NP9": 0x69,
    "Multiply": 0x6A,
    "Add": 0x6B,
    "Separator": 0x6C,
    "Subtract": 0x6D,
    "Decimal": 0x6E,
    "Divide": 0x6F,
    "F1": 0x70,
    "F2": 0x71,
    "F3": 0x72,
    "F4": 0x73,
    "F5": 0x74,
    "F6": 0x75,
    "F7": 0x76,
    "F8": 0x77,
    "F9": 0x78,
    "F10": 0x79,
    "F11": 0x7A,
    "F12": 0x7B,
    "F13": 0x7C,
    "F14": 0x7D,
    "F15": 0x7E,
    "F16": 0x7F,
    "F17": 0x80,
    "F18": 0x81,
    "F19": 0x82,
    "F20": 0x83,
    "F21": 0x84,
    "F22": 0x85,
    "F23": 0x86,
    "F24": 0x87,
    "NumLock": 0x90,
    "ScrollLock": 0x91,
    "LeftShift": 0xA0,
    "RightShift": 0xA1,
    "LeftControl": 0xA2,
    "RightControl": 0xA3,
    "LeftAlt": 0xA4,
    "RightAlt": 0xA5,
    "LeftMenu": 0xA4,
    "RightMenu": 0xA5,
    "BrowserBack": 0xA6,
    "BrowserForward": 0xA7,
    "BrowserRefresh": 0xA8,
    "BrowserStop": 0xA9,
    "BrowserSearch": 0xAA,
    "BrowserFavorites": 0xAB,
    "BrowserHome": 0xAC,
    "VolumeMute": 0xAD,
    "VolumeDown": 0xAE,
    "VolumeUp": 0xAF,
    "MediaNext Track": 0xB0,
    "MediaPrevious Track": 0xB1,
    "MediaStop": 0xB2,
    "MediaPlay": 0xB3,
    "LaunchMail": 0xB4,
    "LaunchMedia Select": 0xB5,
    "LaunchApp1": 0xB6,
    "LaunchApp2": 0xB7,
    "OEM1": 0xBA,
    "OEMPlus": 0xBB,
    "OEMComma": 0xBC,
    "OEMMinus": 0xBD,
    "OEMPeriod": 0xBE,
    "OEM2": 0xBF,
    "OEM3": 0xC0,
    "OEM4": 0xDB,
    "OEM5": 0xDC,
    "OEM6": 0xDD,
    "OEM7": 0xDE,
    "OEM8": 0xDF,
    "OEM102": 0xE2,
    "ProcessKey": 0xE5,
    "Packet": 0xE7,
    "Attn": 0xF6,
    "CrSel": 0xF7,
    "ExSel": 0xF8,
    "EraseEOF": 0xF9,
    "Play": 0xFA,
    "Zoom": 0xFB,
    "PA1": 0xFD,
    "0x08":"0x08",
    "0x09":"0x09",
    "0x0C":"0x0C",
    "0x0D":"0x0D",
    "0x10":"0x10",
    "0x11":"0x11",
    "0x12":"0x12",
    "0x13":"0x13",
    "0x14":"0x14",
    "0x1B":"0x1B",
    "0x20":"0x20",
    "0x21":"0x21",
    "0x22":"0x22",
    "0x23":"0x23",
    "0x24":"0x24",
    "0x25":"0x25",
    "0x26":"0x26",
    "0x27":"0x27",
    "0x28":"0x28",
    "0x29":"0x29",
    "0x2A":"0x2A",
    "0x2B":"0x2B",
    "0x2C":"0x2C",
    "0x2D":"0x2D",
    "0x2E":"0x2E",
    "0x30":"0x30",
    "0x31":"0x31",
    "0x32":"0x32",
    "0x33":"0x33",
    "0x34":"0x34",
    "0x35":"0x35",
    "0x36":"0x36",
    "0x37":"0x37",
    "0x38":"0x38",
    "0x39":"0x39",
    "0x41":"0x41",
    "0x42":"0x42",
    "0x43":"0x43",
    "0x44":"0x44",
    "0x45":"0x45",
    "0x46":"0x46",
    "0x47":"0x47",
    "0x48":"0x48",
    "0x49":"0x49",
    "0x4A":"0x4A",
    "0x4B":"0x4B",
    "0x4C":"0x4C",
    "0x4D":"0x4D",
    "0x4E":"0x4E",
    "0x4F":"0x4F",
    "0x50":"0x50",
    "0x51":"0x51",
    "0x52":"0x52",
    "0x53":"0x53",
    "0x54":"0x54",
    "0x55":"0x55",
    "0x56":"0x56",
    "0x57":"0x57",
    "0x58":"0x58",
    "0x59":"0x59",
    "0x5A":"0x5A",
    "0x5B":"0x5B",
    "0x5C":"0x5C",
    "0x5D":"0x5D",
    "0x5F":"0x5F",
    "0x60":"0x60",
    "0x61":"0x61",
    "0x62":"0x62",
    "0x63":"0x63",
    "0x64":"0x64",
    "0x65":"0x65",
    "0x66":"0x66",
    "0x67":"0x67",
    "0x68":"0x68",
    "0x69":"0x69",
    "0x6A":"0x6A",
    "0x6B":"0x6B",
    "0x6C":"0x6C",
    "0x6D":"0x6D",
    "0x6E":"0x6E",
    "0x6F":"0x6F",
    "0x70":"0x70",
    "0x71":"0x71",
    "0x72":"0x72",
    "0x73":"0x73",
    "0x74":"0x74",
    "0x75":"0x75",
    "0x76":"0x76",
    "0x77":"0x77",
    "0x78":"0x78",
    "0x79":"0x79",
    "0x7A":"0x7A",
    "0x7B":"0x7B",
    "0x7C":"0x7C",
    "0x7D":"0x7D",
    "0x7E":"0x7E",
    "0x7F":"0x7F",
    "0x80":"0x80",
    "0x81":"0x81",
    "0x82":"0x82",
    "0x83":"0x83",
    "0x84":"0x84",
    "0x85":"0x85",
    "0x86":"0x86",
    "0x87":"0x87",
    "0x90":"0x90",
    "0x91":"0x91",
    "0xA0":"0xA0",
    "0xA1":"0xA1",
    "0xA2":"0xA2",
    "0xA3":"0xA3",
    "0xA4":"0xA4",
    "0xA5":"0xA5",
    "0xA6":"0xA6",
    "0xA7":"0xA7",
    "0xA8":"0xA8",
    "0xA9":"0xA9",
    "0xAA":"0xAA",
    "0xAB":"0xAB",
    "0xAC":"0xAC",
    "0xAD":"0xAD",
    "0xAE":"0xAE",
    "0xAF":"0xAF",
    "0xB0":"0xB0",
    "0xB1":"0xB1",
    "0xB2":"0xB2",
    "0xB3":"0xB3",
    "0xB4":"0xB4",
    "0xB5":"0xB5",
    "0xB6":"0xB6",
    "0xB7":"0xB7",
    "0xBA":"0xBA",
    "0xBB":"0xBB",
    "0xBC":"0xBC",
    "0xBD":"0xBD",
    "0xBE":"0xBE",
    "0xBF":"0xBF",
    "0xC0":"0xC0",
    "0xDB":"0xDB",
    "0xDC":"0xDC",
    "0xDD":"0xDD",
    "0xDE":"0xDE",
    "0xDF":"0xDF",
    "0xE2":"0xE2",
    "0xE5":"0xE5",
    "0xE7":"0xE7",
    "0xF6":"0xF6",
    "0xF7":"0xF7",
    "0xF8":"0xF8",
    "0xF9":"0xF9",
    "0xFA":"0xFA",
    "0xFB":"0xFB",
    "0xFD":"0xFD"
}

    asyncio.run(async_task())
    
    
    
