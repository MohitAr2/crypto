# import socket
# import random
# from power_mod import power_mod


# # just make comms bw them 

# # taken embedded vlaues in this system where all know that these are the p and g values
# # even the attacker 
# p = 173 
# # the prime num both sides known alice sends this to bob too
# g = 87
# XA = random.randint(1,p-1) # private key of alice
# YA = power_mod(g,XA,p) # g power xa mod p 
# # the publiuc key to be sent to bob 

# # gets YB val from bob


import socket
from power_mod import power_mod

p = 173
g = 55
XA = 51  # Alice's private key

def alice():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8080))

    # Generate Alice's public key
    YA = power_mod(g, XA, p)
    print(f"[Alice] Public key: {YA}")
    client.send(str(YA).encode())  # Send to MITM

    # Receive Bob's public key (Actually from MITM)
    YB = int(client.recv(1024).decode())
    print(f"[Alice] Received public key: {YB}")

    # Compute shared secret
    S = power_mod(YB, XA, p)
    print(f"[Alice] Computed Secret Key: {S}")

alice()

