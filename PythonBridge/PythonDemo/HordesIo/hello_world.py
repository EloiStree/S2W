## TOOLBOX
import time
import socket
import struct

#VARIABLE
left = 1037
up = 1038
right = 1039
down = 1040
jump = 1032

target_ipv4= "127.0.0.1"
target_port= 7073

#FUNCTION
def send_integer_to_target(integer_to_send:int):
    network_target = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = struct.pack("<i", integer_to_send)
    network_target.sendto(data, (target_ipv4, target_port))
    
def press_key(key_to_press:int):
    send_integer_to_target(key_to_press)
    print("PRESS: ",key_to_press)

def release_key(key_to_press:int):
    send_integer_to_target(key_to_press+1000)
    print("RELEASE: ",key_to_press+1000)

#MAIN CODE  
# CTRL K C Comment 
# CTRL K U  uncomment
def jump_n_time(jump_count:int):
    for i in range(jump_count):
        press_key(jump)
        time.sleep(1)
        release_key(jump)
        time.sleep(1)

def walk_for_n_seconds(time_to_walk_in_seconds:float):
    press_key(up) # Press up arrow
    time.sleep(time_to_walk_in_seconds)
    release_key(up) # Release up arrow after n seconds

def walk_for_n_meters(meters:float):
    walk_for_n_seconds(meters/5.2)


    
def walk_backward_for_n_seconds(time_to_walk_in_seconds:float):
    press_key(down) 
    time.sleep(time_to_walk_in_seconds)
    release_key(down) 

def walk_backward_for_n_meters(meters:float):
    walk_backward_for_n_seconds(meters/2.6) # To add

# jump_n_time(5)

# walk_for_n_seconds(10)
# (1372 - 1320)/10 = 5.2 meter per seconds.

# walk_for_n_meters(10)


def rotate_for_n_seconds_left(time_to_rotate_in_seconds:float):
    press_key(left) 
    time.sleep(time_to_rotate_in_seconds)
    release_key(left) 

def rotate_for_n_degree_left(time_to_rotate_in_degree:float):
    rotate_for_n_seconds_left(time_to_rotate_in_degree/172.2)


def rotate_for_n_seconds_right(time_to_rotate_in_seconds:float):
    press_key(right) 
    time.sleep(time_to_rotate_in_seconds)
    release_key(right) 

def rotate_for_n_degree_right(time_to_rotate_in_degree:float):
    rotate_for_n_seconds_right(time_to_rotate_in_degree/172.2)

# Ready to count ? 4.8 for 10 seconds
#28.7 / 60 seconds = 172,2 degree per seconds 
# rotate_for_n_seconds_left(60)
# rotate_for_n_degree_left(180)

# rotate_for_n_degree_left(90)
# rotate_for_n_degree_right(180)
# rotate_for_n_degree_left(90)

# # Tadam
# walk_for_n_meters(10)


walk_backward_for_n_meters(10)
