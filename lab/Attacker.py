# import socket
# from power_mod import power_mod

# p = 173 # somehow stole this information 
# g = 87




import socket
import threading
from power_mod import power_mod

# Prime and base values known by all via the embeeded system lets say this is known by attaacker
p = 173 
g = 55  

# Attacker's private keys (to impersonate Alice and Bob)
xa = 44  # Private Alice
xb = 32 # Private Bob

def handle_alice(conn_alice, conn_bob):
    global g, p, xa
    # Alice's public key stolen
    YA = int(conn_alice.recv(1024).decode())  
    print(f"[MITM] Intercepted Alice's public key: YA = {YA}")

    # fake public key for Alice thinking bob
    Y_fake = power_mod(g, xa, p)  
    conn_alice.send(str(Y_fake).encode()) 
    # Send fake key to Alice
    # shared key with alice thinking bob the separate conncetion made
    S1 = power_mod(YA, xa, p)  
    print(f"[MITM] Shared Key with Alice: {S1}")

    # Forward YA (Alice's key) to Bob
    conn_bob.send(str(YA).encode())

def handle_bob(conn_alice, conn_bob):
    """ Handles communication with Bob and intercepts Diffie-Hellman keys """
    global g, p, xb

    # Receive Bob's public key
    YB = int(conn_bob.recv(1024).decode())  
    print(f"[MITM] Intercepted Bob's public key: YB = {YB}")

    # Generate MITM's fake public key for Bob
    Y_fake = power_mod(g, xb, p)  
    conn_bob.send(str(Y_fake).encode())  # Send fake key to Bob

    # Compute secret key (MITM key with Bob)
    S2 = power_mod(YB, xb, p)  
    print(f"[MITM] Secret Key with Bob: {S2}")

    # Forward YB (Bob's key) to Alice
    conn_alice.send(str(YB).encode())

def start_mitm():
    """ Starts MITM server that connects Alice and Bob """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8080))
    server.listen(2)

    print("[MITM] Waiting for Alice and Bob...")
    conn_alice, _ = server.accept()
    print("[MITM] Alice connected")

    conn_bob, _ = server.accept()
    print("[MITM] Bob connected")
    threading.Thread(target=handle_alice, args=(conn_alice, conn_bob)).start()
    threading.Thread(target=handle_bob, args=(conn_alice, conn_bob)).start()

if __name__ == "__main__":
    start_mitm()