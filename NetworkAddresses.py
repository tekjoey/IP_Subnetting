import random

def from_long_to_dot_dec(long_address):
    long_a = long_address[:8]
    long_b = long_address[8:16]
    long_c = long_address[16:24]
    long_d = long_address[24:]
    return f"{int(long_a, 2)}.{int(long_b, 2)}.{int(long_c, 2)}.{int(long_d, 2)}"

a = random.randint(1,255)
b = random.randint(1,255)
c = random.randint(1,255)
d = random.randint(1,255)

e = random.randint(1,32)

given_decimal_address = f"{a}.{b}.{c}.{d}/{e}"
given_binary_address_seperated = f"{a:08b} {b:08b} {c:08b} {d:08b} / {'1' * e}"
given_binary_address_unseperated = f"{a:08b}{b:08b}{c:08b}{d:08b}"

network_portion = given_binary_address_unseperated[:e]
host_portion = given_binary_address_unseperated[e:]
host_len = len(host_portion)

binary_network_address = f"{network_portion}{'0' * host_len}"
decimal_network_address = from_long_to_dot_dec(binary_network_address)

binary_broadcast_address = f"{network_portion}{'1' * host_len}"
decimal_broadcast_address = from_long_to_dot_dec(binary_broadcast_address)

binary_first_host = f"{network_portion}{'0' * (host_len - 1)}{'1'}"
decimal_first_host = from_long_to_dot_dec(binary_first_host)


binary_last_host = f"{network_portion}{'1' * (host_len - 1)}{'0'}"
decimal_last_host = from_long_to_dot_dec(binary_last_host)

print(given_decimal_address)
x = input("Press any key to continue") 
print("Network address:" ,decimal_network_address)
print("Broadcast address:", decimal_broadcast_address)
print("First Host Address:", decimal_first_host)

print("Last Host Address:", decimal_last_host)


""""need
given address/mask /
network address /
broadcast address /
First usable host
last usable host """



