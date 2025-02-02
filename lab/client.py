import socket
import numpy as np
from ciphers.Caesar import encrypt_caesar
from ciphers.Hill import encrypt_hill
from ciphers.Play_Fair import encrypt_playfair
from ciphers.Rail_Fence import encrypt_rail_fence
from ciphers.Row_Column_transposition import encrypt_row_column_transposition
from ciphers.Vernam import encrypt_vernam
from ciphers.Vignere import encrypt_vignere
from ciphers.DES import encrypt_DES

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8080))
    print("Connected to the server")
    while True:
        mess = input("Plain text (if in DES give hexadecimal of size 16) for example \"123456ABCD132536\" : ")
        print("Choose type of encryption:")
        print("0 for PlayFair")
        print("1 for Hill")
        print("2 for Rail Fence")
        print("3 for Row-Column Cipher")
        print("4 for Vernam")
        print("5 for Vigenere")
        print("6 for Caesar")
        print("7 for DES")
        a = int(input("Enter your choice: "))
        
        
        client_socket.send(str(a).encode('utf-8')) 
        # sending the type of encryption used
        
        
        if a == 0:
            k = input("Enter the key (string) example \"abcdefg\": ")
            message = encrypt_playfair(mess, k)
            print("PlayFair encryption selected.")
        elif a == 1:
            k = input("Enter the key (string) example \"[[1,2],[1,2]]\": ") # chcek for square matrix input 
            message = encrypt_hill(mess, np.array(eval(k)))
            print("Hill encryption selected.")
        elif a == 2:
            k = input("Enter the key (as an int) example input is -> \"4\" : ")
            depth = int(k)
            message = encrypt_rail_fence(mess, depth)
            print("Rail Fence encryption selected.")
        elif a == 3:
            k = input("Enter the key (as a string): ")
            # key_list = [int(x) for x in k.split()]
            message = encrypt_row_column_transposition(mess, eval(k)) 
            # here issue in code cant fig it out help  in func not here!!! 
            print("Row-Column Cipher encryption selected.")
        elif a == 4:
            k = input("Enter the key (string) example \"[[1,2],[1,2]]\" : ")
            use_uppercase = mess.isupper()
            message = encrypt_vernam(mess, k, use_uppercase)
            print("Vernam encryption selected.")
        elif a == 5:
            k = input("Enter the key (as a string): ")
            message = encrypt_vignere(mess, k)
            print("Vigenere encryption selected.")
        elif a == 6:
            k = input("Enter the key (as an int) example input is -> \"4\" : ")
            shift = int(k)
            message = encrypt_caesar(mess, shift)
            print("Caesar encryption selected.")
        elif a==7:
            k = input("Key should be given (as a string but hexadecimal value of size 16 ) -> \"ABCDEFABCDEF1233\" : ")
            message = encrypt_DES(mess,k,False)
            print("DES encryption selected.")
        else:
            k = input("Enter the key but there is an error now wont matter this is to handle the empty send signal of client")
            print("Invalid choice.")
            continue

        client_socket.send(k.encode('utf-8'))
        print(f"Encrypted_message of {mess} is : {message}")
        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

if __name__ == "__main__":
    start_client()