# import numpy as np 

# def encrypt_hill(hill:str,kee:list[int])->str:
#     out=""
#     # based on size of k 
#     if(len(hill)%len(kee) != 0):
#         hill += 'x'*(len(hill)%len(kee) + 2)
#     oy = []
#     for i in range(0,len(hill),len(kee)):
#         f = list((hill[i:i+len(kee)]))
#         g = []
#         for j in f:
#             g.append(ord(j)-ord('a'))
#         oy.append(g)
#     all = []
#     print("The plain text as a matrix input : ",oy)
#     for i in oy:
#         all.append((np.dot(i,kee))%26)
#     print("After the matrix multiplication with the key in numpy : " , all)
#     for i in all:
#         for k in i: 
#             out += chr(k+97)
#     return out

# def decrypt_hill(hill:str, key:list[int]) -> str:
#     kee = np.array(key) # converts str to list then to np num array int/float type 
#     out = ""
#     n = kee.shape[0] # new concept learned
#     oy = []
#     for i in range(0, len(hill), n):
#         oy.append([ord(char) - 97 for char in hill[i:i+n]])
#     det = int(np.round(np.linalg.det(kee)))
#     det_inv = pow(det, -1, 26)
#     key_inv = (det_inv * np.round(det * np.linalg.inv(kee)).astype(int) % 26) % 26
#     # used net pre def funcs 
#     all = []
#     for i in oy:
#         all.append(np.dot(i, key_inv) % 26)
#     for i in all:
#         for k in i:
#             out += chr(int(k) + 97)
#     return out



import numpy as np

def encrypt_hill(plaintext: str, key: np.ndarray) -> str:
    out = ""
    n = key.shape[0]
    
    # Pad plaintext to be a multiple of the key size
    while len(plaintext) % n != 0:
        plaintext += 'x' 
    
    # Convert plaintext to numerical values
    oy = []
    for i in range(0, len(plaintext), n):
        oy.append([ord(char) - 97 for char in plaintext[i:i+n]])
    
    # Encrypt the plaintext
    all = []
    for i in oy:
        all.append(np.dot(i, key) % 26)
    
    for i in all:
        for k in i:
            out += chr(int(k) + 97)
    
    return out

def decrypt_hill(ciphertext: str, key: np.ndarray) -> str:
    out = ""
    n = key.shape[0]
    
    # Convert ciphertext to numerical values
    oy = []
    for i in range(0, len(ciphertext), n):
        oy.append([ord(char) - 97 for char in ciphertext[i:i+n]])
    
    # Calculate the inverse of the key matrix modulo 26
    det = int(np.round(np.linalg.det(key)))
    det_inv = pow(det, -1, 26)
    key_inv = (det_inv * np.round(det * np.linalg.inv(key)).astype(int) % 26) % 26
    
    # Decrypt the ciphertext
    all = []
    for i in oy:
        all.append(np.dot(i, key_inv) % 26)
    
    for i in all:
        for k in i:
            out += chr(int(k) + 97)
    
    return out

# # Example 1
# plaintext1 = "hello"
# key1 = np.array([[6,1], [13, 12]])
# ciphertext1 = encrypt_hill(plaintext1, key1)
# print(ciphertext1)  # Expected output: "fnlxx" (or similar, depending on padding)

# decrypted1 = decrypt_hill(ciphertext1, key1)
# print(decrypted1)  # Expected output: "hellox"

# # Example 2
# plaintext2 = "attackatdawn"
# key2 = np.array([[3, 3, 2], [2, 3, 1], [1, 1, 1]])
# ciphertext2 = encrypt_hill(plaintext2, key2)
# print(ciphertext2)  # Expected output: "dppxqzqzqzqz" (or similar, depending on padding)

# decrypted2 = decrypt_hill(ciphertext2, key2)
# print(decrypted2)  # Expected output: "attackatdawn"