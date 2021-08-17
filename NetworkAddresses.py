'''
NetworkAddresses.py by tekjoey
Created to help me study for the Network+ exam.
Commited 17 August 2021
MIT licenced
Script 1 of 1

For help solving subnetting questions, check out Professor Messor on YouTube
'''

import random

#this function takes a 32 bit binary IP address and converts it to doted decimal notation.
def from_long_to_dot_dec(long_address):
    long_a = long_address[:8]
    long_b = long_address[8:16]
    long_c = long_address[16:24]
    long_d = long_address[24:]
    return f"{int(long_a, 2)}.{int(long_b, 2)}.{int(long_c, 2)}.{int(long_d, 2)}"

#a-d are the 4 octets of the IP address
a = random.randint(1,255)
b = random.randint(1,255)
c = random.randint(1,255)
d = random.randint(1,255)

#e is the subnet mask, expressed as CIDR notation
e = random.randint(1,32)

#the dotted-decimal notation slash subnet mask
given_decimal_address = f"{a}.{b}.{c}.{d}/{e}"

#convert the IP adddress to binary
given_binary_address = f"{a:08b}{b:08b}{c:08b}{d:08b}"

#seperate binary IP address to network and host portions
network_portion = given_binary_address[:e]
host_portion = given_binary_address[e:]
host_len = len(host_portion)

#make network portion the full 32 bits, and convert back to decimal to display
binary_network_address = f"{network_portion}{'0' * host_len}"
decimal_network_address = from_long_to_dot_dec(binary_network_address)

#calculate broadcast address in binary then convert to decimal
binary_broadcast_address = f"{network_portion}{'1' * host_len}"
decimal_broadcast_address = from_long_to_dot_dec(binary_broadcast_address)

#calculate the first usable host address in binary and convert to decimal
binary_first_host = f"{network_portion}{'0' * (host_len - 1)}{'1'}"
decimal_first_host = from_long_to_dot_dec(binary_first_host)

#calculate last usable host address in binary and convert to decimal
binary_last_host = f"{network_portion}{'1' * (host_len - 1)}{'0'}"
decimal_last_host = from_long_to_dot_dec(binary_last_host)

#show results to user
print(given_decimal_address)
x = input("Press any key to see the answer") 
print("Network address:" ,decimal_network_address)
print("Broadcast address:", decimal_broadcast_address)
print("First Host Address:", decimal_first_host)
print("Last Host Address:", decimal_last_host)

#SoliDeoGloria
