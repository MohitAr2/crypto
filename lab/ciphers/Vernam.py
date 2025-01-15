def encrypt_vernam(plaintext, key, use_uppercase):
    base = ord('A') if use_uppercase else ord('a')
    ciphertext = ''.join(chr(((ord(p) - base) ^ (ord(k) - base)) % 26 + base) for p, k in zip(plaintext, key))
    return ciphertext

def decrypt_vernam(ciphertext, key, use_uppercase):
    base = ord('A') if use_uppercase else ord('a')
    decrypted_text = ''.join(chr(((ord(c) - base) ^ (ord(k) - base)) % 26 + base) for c, k in zip(ciphertext, key))
    return decrypted_text

# # XOR gate
# plaintext1 = "HELLO" # eitehr all caps or all small imp can improve on this by checking each letter and - ord('A' or 'a') too much work
# key1 = "XMCKL"
# ciphertext1 = encrypt_vernam(plaintext1, key1, use_uppercase=True)
# print(ciphertext1)  # Expected output: "EQNVZ"

# decrypted1 = decrypt_vernam(ciphertext1, key1, use_uppercase=True)
# print(decrypted1)  # Expected output: "HELLO"

# # Example 2
# plaintext2 = "attackatdawn"
# key2 = "XMCKLXMCKLXM"
# ciphertext2 = encrypt_vernam(plaintext2, key2, use_uppercase=False)
# print(ciphertext2)  # Expected output: "xkzjzlxkzjzl"

# decrypted2 = decrypt_vernam(ciphertext2, key2, use_uppercase=False)
# print(decrypted2)  # Expected output: "attackatdawn"