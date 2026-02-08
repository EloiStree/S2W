
# SILK SONG DONT ACCEPT FAKE INPUT APPARENTLY


import socket
import struct
import time
import random

int_power1=1049

ip_target ="127.0.0.1"
ip_target_port = 7073

int_index = [1,2,3,4,5,6]



int_arrow_left=1037
int_arrow_right=1039
int_arrow_up=1038
int_arrow_down=1040
int_arrow_enter=1013
int_arrow_escape=1027
int_key_z_jump=1090
int_key_x_attack=1088
int_key_a_interact=1065
int_key_space= 1032




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

def send_action_and_wait_time(int_value,t):
    for i in int_index:
        send_index_integer_command(i, int_value)
    time.sleep(t)
    for i in int_index:
        send_index_integer_command(i, int_value+1000)
    time.sleep(t)

jump =0
while True:
        jump+=1
        time_between=0.5
        send_action_and_wait_time(int_arrow_left,time_between)
        send_action_and_wait_time(int_key_x_attack,time_between)
        send_action_and_wait_time(int_arrow_right,time_between)
        send_action_and_wait_time(int_key_x_attack,time_between)
        send_action_and_wait_time(int_arrow_up,time_between)
        send_action_and_wait_time(int_key_x_attack,time_between)
        send_action_and_wait_time(int_arrow_down,time_between)
        send_action_and_wait_time(int_key_x_attack,time_between)
        send_action_and_wait_time(int_key_z_jump,time_between)


        

# int_arrow_left=1037
# int_arrow_right=1039
# int_arrow_up=1038
# int_arrow_down=1040
# int_arrow_enter=1013
# int_arrow_escape=1027
# int_key_z_jump=1090
# int_key_x_attack=1088
# int_key_a_interact=1065
# int_key_space= 1032
        
        

        
    
       


