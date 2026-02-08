
import socket
import struct
import time
import random


int_character_index =1
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
int_heal=1055
int_shield=1056
int_select_enemy=1057
int_interaction= 1103
int_last_target= 1111
int_move_right= 1102
int_move_left= 1100
int_move_back= 1101


ip_target ="127.0.0.1"
ip_target_port = 7073

int_index = [2,3,4,5]
int_index = [1,2]


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
    time.sleep(1.9)

def send_action_and_wait_time(int_value,t):
    for i in int_index:
        send_index_integer_command(i, int_value)
    time.sleep(t)
    for i in int_index:
        send_index_integer_command(i, int_value+1000)



while True:


    bool_boris=True
    if bool_boris:

        # send_action(int_jump)
        if random.random() > 0.9:
            send_action(int_jump)
        # Select Boris
        """
        /targetexact Silent Boris
        /targetexact Lindel the Snatcher
        """
        print("Select Boris")
        send_action(int_power1)
        time.sleep(0.1)
        # Send pet
        print("Send pet")
        send_action(int_power2)
        time.sleep(14)
        # Select Lindel
        print("Select Lindel")
        send_action(int_power3)
        time.sleep(0.1)
        # Send pet
        print("Send pet")
        send_action(int_power4)
        time.sleep(8)
        # Make pet come back
        print("Make pet come back")
        send_action(int_power5)
        time.sleep(20)
        # Heal Pet
        print("Heal Pet")
        send_action(int_power6)
        time.sleep(0.1)
        # Rez pet just in case
        print("Rez Pet")
        send_action(int_power7)
        time.sleep(1.9)
        # hide
        print("hide")
        send_action(int_power8)
        time.sleep(0.5)
        # Wait them to repop
        print("Wait them to repop")
        time.sleep(50.0)
        
        

    bool_classic = False
    if bool_classic:
        send_action( int_tab) 
        time.sleep(0.1)
        for i in range(2):
                send_action( int_power2)
                time.sleep(0.2)
                send_action_and_wait( int_power1)
        send_action(int_last_target)
        send_action_and_wait(int_interaction)

    bool_heal_loop= False
    if bool_heal_loop:
        send_action(int_tab)
        send_action_and_wait( int_power2)
        send_action( int_select_enemy)
        send_action_and_wait( int_power2)

    for i in range(4):
        send_action( int_select_enemy)
        time.sleep(0.1)
        send_action_and_wait( int_power1)
        
    send_action_and_wait(int_heal)
    send_action_and_wait(int_shield)
    send_action(int_last_target)
    send_action_and_wait(int_interaction)

    


    bool_dot_mode=False
    if bool_dot_mode:
        for i in range(6):
            send_action( int_tab)
            time.sleep(0.1)
            send_action_and_wait( int_power1)
        for i in range(4):
            send_action_and_wait( int_power2)
    
    
    bool_back_fire_mode = False
    if bool_back_fire_mode:
        send_press_key_command(int_move_back)
        send_action( int_tab)
        time.sleep(0.1)
        for i in range(2):
                send_action_and_wait( int_power2)
                send_action_and_wait( int_power1)
        send_action(int_last_target)
        send_action_and_wait(int_interaction)
        bool_left =random.choice([True,False])
        if bool_left:
            send_action_and_wait_time( int_move_left,0.5+random.random()*0.5)
        else:
            send_action_and_wait_time( int_move_right,0.5+random.random()*0.5)
        #send_action_and_wait_time(1+ int_move_back,random.random()*0.5)
        send_release_key_command(int_move_back)


    
       


