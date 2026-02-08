
import socket
import struct
import time

def send_index_integer_command_with_ip(ip_of_computer, port_of_application, id_player, id_key):
    message = struct.pack('<iiq', id_player, id_key, 0) # 1010101110101....00111101100
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (ip_of_computer, port_of_application))
    sock.close()

print("Hello World")
age=36

# This is a comment that won't be executed

"""
I am a commentary on several lines
Hello guys, this is a Python script
"""

print(age)

target_ip ="127.0.0.1"
target_port = 7073
key_tab = 1009
key_power1 = 1049
player_id_targeted = 0


while True:
      print("Start tab  ")
      send_index_integer_command_with_ip(target_ip, target_port, player_id_targeted, key_tab)
      time.sleep(0.1)  
      print("Stop tab  ")
      send_index_integer_command_with_ip(target_ip, target_port, player_id_targeted, key_tab+1000)
      time.sleep(0.1)  
      for counting in range(0, 3):
            print("Start power 1 " + str(counting))
            send_index_integer_command_with_ip(target_ip, target_port, player_id_targeted, key_power1)
            time.sleep(0.5)
            print("Stop power 1 " + str(counting))
            send_index_integer_command_with_ip(target_ip, target_port, player_id_targeted, key_power1+1000)
            time.sleep(1.8)

      



