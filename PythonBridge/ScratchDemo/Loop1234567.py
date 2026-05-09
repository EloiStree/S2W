
import socket
import struct
import time
import random


int_character_index =0

int_tab= 1009
int_jump= 1032
int_power1=1049
int_power2=1050
int_power3=1051
int_power4=1052
int_power5=1053
int_power6=1054
int_power7=1055
int_power8=1056
int_power9=1057
int_power0=1048
int_home=1035
int_end=1036
int_delete=1046
int_page_up=1033
int_page_down=1034
int_heal=1055
int_shield=1056
int_select_enemy=1057
int_interaction= 1103
int_last_target= 1111
int_move_right= 1102
int_move_left= 1100
int_move_back= 1101


int_numpad_0= 1096
int_numpad_1= 1097
int_numpad_2= 1098
int_numpad_3= 1099
int_numpad_4= 1100
int_numpad_5= 1101
int_numpad_6= 1102
int_numpad_7= 1103
int_numpad_8= 1104
int_numpad_9= 1105
int_numpad_multiply= 1106
int_numpad_add= 1107
int_numpad_separtor= 1108
int_numpad_substract= 1109
int_numpad_decimal= 1110
int_numpad_divide= 1111

int_interaction = 1103

int_arrow_up= 1038
int_arrow_right= 1039
int_arrow_down= 1040
int_arrow_left= 1037
int_escape= 1027

int_f1 = 1112
int_f2 = 1113
int_f3 = 1114
int_f4 = 1115
int_f5 = 1116
int_f6 = 1117
int_f7 = 1118
int_f8 = 1119
int_f9 = 1120
int_f10 = 1121
int_f11 = 1122
int_f12 = 1123

ip_target ="127.0.0.1"
ip_target_port = 7074

int_index = [0]
#int_index = [2]

time_between_action_min=0.3
time_between_action_max=0.5


def get_time_to_wait_default():
    return random.uniform(time_between_action_min, time_between_action_max)


def send_index_integer_command( int1, int2):
    message = struct.pack('<iiq', int1, int2, 0)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (ip_target, ip_target_port))
    sock.close()

# Sent Little Endian Integer to target
def send_index_integer_command_with_ip(ip, port, int1, int2):
    message = struct.pack('<iiq', int1, int2, 0)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (ip, port))
    sock.close()


def send_press_key_command( int1):
    for i in int_index:
        send_index_integer_command(i, int1)
def send_release_key_command( int1):
    for i in int_index:
        send_index_integer_command(i, int1+1000)

def send_action(int_value):
    for i in int_index:
        send_index_integer_command(i, int_value)
        send_index_integer_command(i, int_value+1000)   

def send_action_and_wait(int_value):
    for i in int_index:
        send_index_integer_command(i, int_value)
        send_index_integer_command(i, int_value+1000)
    time.sleep(get_time_to_wait_default())

def send_action_and_wait_time(int_value,t):
    for i in int_index:
        send_index_integer_command(i, int_value)
    time.sleep(t)
    for i in int_index:
        send_index_integer_command(i, int_value+1000)

def follow_and_target():
    
        send_action( int_arrow_up)
        time.sleep(0.1)
        send_action(int_delete)
        time.sleep(0.1)
        send_action(int_tab)

while True:


    bool_hunter_loop = True
    if bool_hunter_loop:


        send_action( int_tab)
        send_action(int_interaction)
        time.sleep(0.1)
        send_action_and_wait(int_power1) 
        send_action_and_wait(int_power2) 
        send_action_and_wait(int_power3) 
        send_action_and_wait(int_power4) 
        send_action( int_tab)
        send_action(int_interaction)
        send_action_and_wait(int_power5) 
        send_action_and_wait(int_power6) 
        send_action_and_wait(int_power7) 
        



    
       


