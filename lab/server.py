import socket
import numpy as np
from ciphers.Caesar import decrypt_caesar
from ciphers.Hill import decrypt_hill
from ciphers.Play_Fair import decrypt_playfair
from ciphers.Rail_Fence import decrypt_rail_fence
from ciphers.Row_Column_transposition import decrypt_row_column_transposition
from ciphers.Vernam import decrypt_vernam
from ciphers.Vignere import decrypt_vignere
from ciphers.DES import decrypt_DES
from ciphers.AES import decrypt_AES

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)
    print("Server is listening on port 8080")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    while True:
        a = client_socket.recv(1024).decode('utf-8')
        k = client_socket.recv(1024).decode('utf-8')
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Client sent encrypted: {message}")
        
        if a == '0':  # PlayFair
            fin = decrypt_playfair(message, k)
            print("PlayFair decryption selected.")
        elif a == '1':  # Hill
            fin = decrypt_hill(message, np.array(eval(k)))
            print("Hill decryption selected.")
        elif a == '2':  # Rail Fence
            depth = int(k)
            fin = decrypt_rail_fence(message, depth)
            print("Rail Fence decryption selected.")
        elif a == '3':  # Row-Column Transposition
            key_list = eval(k)
            fin = decrypt_row_column_transposition(message, key_list)
            print("Row-Column Transposition decryption selected.")
        elif a == '4':  # Vernam
            use_uppercase = message.isupper()
            fin = decrypt_vernam(message, k, use_uppercase)
            print("Vernam decryption selected.")
        elif a == '5':  # Vigenere
            fin = decrypt_vignere(message, k)
            print("Vigenere decryption selected.")
        elif a == '6':  # Caesar
            shift = int(k)
            fin = decrypt_caesar(message, shift)
            print("Caesar decryption selected.")
        elif a == '7':  # DES
            fin = decrypt_DES(message, k)
            print("DES decryption selected.")
        elif a == '8':
            fin = decrypt_AES(message,k)
            print("AES decryption selected.")
            # has errors here inverse logic mistakes there cant fig out where ?
        else:
            fin = "Invalid encryption type."
            print("Invalid decryption type selected.")
        
        print(f"Decrypted message: {fin}")
        response = "Your message has been received .. close socket ctrl C to exit"
        client_socket.send(response.encode('utf-8'))
    
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

