def encrypt_vignere(a: str, b: str) -> str:  # b is the key
    # a = iajslkdja b = best loop for
    # p[i] + k[i] mod 26 add mod size if exceeds
    cd = ""  # out str
    for i in range(len(a)):
        # print(ord(a[i]) , ord(b[i % len(b)]))
        if 'a' <= a[i] <= 'z':
            c = (ord(a[i]) - ord('a') + ord(b[i % len(b)]) - ord('a')) % 26 + ord('a')
        elif 'A' <= a[i] <= 'Z':
            c = (ord(a[i]) - ord('A') + ord(b[i % len(b)]) - ord('A')) % 26 + ord('A')
        cd += chr(c)
        # print(c)
    return cd

def decrypt_vignere(a: str, b: str) -> str:  # b is the key
    cd = ""  # out str
    for i in range(len(a)):
        if 'a' <= a[i] <= 'z':
            c = (ord(a[i]) - ord('a') - (ord(b[i % len(b)]) - ord('a'))) % 26 + ord('a')
        elif 'A' <= a[i] <= 'Z':
            c = (ord(a[i]) - ord('A') - (ord(b[i % len(b)]) - ord('A'))) % 26 + ord('A')
        cd += chr(c)
    return cd

# # Example 1
# plaintext1 = "hello"
# key1 = "key"
# ciphertext1 = encrypt_vignere(plaintext1, key1)
# print(ciphertext1)  # Expected output: "riijv"

# decrypted1 = decrypt_vignere(ciphertext1, key1)
# print(decrypted1)  # Expected output: "hello"

# # Example 2
# plaintext2 = "ATTACKATDAWN"
# key2 = "LEMON"
# ciphertext2 = encrypt_vignere(plaintext2, key2)
# print(ciphertext2)  # Expected output: "LXFOPVEFRNHR"

# decrypted2 = decrypt_vignere(ciphertext2, key2)
# print(decrypted2)  # Expected output: "ATTACKATDAWN"