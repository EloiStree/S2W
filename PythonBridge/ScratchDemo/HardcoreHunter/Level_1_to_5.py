
import socket
import struct
import time
import random

int_power1=1049

ip_target ="127.0.0.1"
ip_target_port = 7073

int_index = [1,2,3,4,5,6]


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

jump =0
while True:
        jump+=1

        for i in range(1, 6):
            send_action_and_wait_time(1049, 1.75)
            time.sleep(0.1)
            send_action_and_wait_time(1050, 1.75)
            time.sleep(0.1)
            send_action_and_wait_time(1070,0.1)
            time.sleep(0.1)
            
        time.sleep(0.1)
        send_action_and_wait_time(1051,0.1)
        
        time.sleep(0.1)
        if jump%60==0:
            #send_action_and_wait_time(1032,1.9)
            send_action_and_wait_time(1088,1.9)
        
        

        
    
       


