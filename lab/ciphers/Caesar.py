def encrypt_caesar(a: str, k: int) -> str:
    b = ""
    for i in range(len(a)):
        l = ord(a[i])
        if 'a' <= a[i] <= 'z':
            l = (l - ord('a') + k) % 26 + ord('a')
        elif 'A' <= a[i] <= 'Z':
            l = (l - ord('A') + k) % 26 + ord('A')
        b += chr(l)
    return b


def decrypt_caesar(s: str, k: int) -> str:
    out = ""
    for i in range(len(s)):
        t = ord(s[i])
        if 'a' <= s[i] <= 'z':
            t = (t - ord('a') - k) % 26 + ord('a')
        elif 'A' <= s[i] <= 'Z': # caps input also handled
            t = (t - ord('A') - k) % 26 + ord('A')
        out += chr(t)
    return out

# # Example 1
# plaintext1 = "hello"
# key1 = 3
# ciphertext1 = encrypt_caesar(plaintext1, key1)
# print(ciphertext1)  # khoor

# decipher1 = decrypt_caesar(ciphertext1,key1)
# print(decipher1) #hello

# # Example 2
# plaintext2 = "CaesarCipher"
# key2 = 5
# ciphertext2 = encrypt_caesar(plaintext2, key2) # key is shared between server and client
# print(ciphertext2)  # HfjxfwHnumjw

# decipher2 = decrypt_caesar(ciphertext2,key2)
# print(decipher2) #CaesarCipher
