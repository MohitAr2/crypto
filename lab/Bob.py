# import socket
# import random
# from power_mod import power_mod


# p = 173 
# # the prime num both sides known alice sends this to bob too
# g = 87
# XB = random.randint(1,p-1) # private key of bob
# YB = power_mod(g,XB,p) 
# # g power xa mod p 
# # public key of bob 

# # gets YA val from alice 

# YA = 0

import socket
from power_mod import power_mod
p = 173
g = 55
XB = 41  # Bob's private key
def bob():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8080))
    # Generate Bob's public key
    YB = power_mod(g, XB, p)
    print(f"[Bob] Public key: {YB}")
    client.send(str(YB).encode()) 
     # Send to MITM cause he has intercepted thinking this is alice btw
    # Receive Alice's public key (Actually from MITM)
    YA = int(client.recv(1024).decode())
    print(f"[Bob] Received public key: {YA}")
    # Compute shared secret with attacker ehere whcih bob thinks is alice
    S = power_mod(YA, XB, p)
    print(f"[Bob] Computed Secret Key: {S}")

bob()
