def encrypt_row_column_transposition(a:str,k:list[int])->str:
    out = ""
    imp = {}
    for i in k:
        imp[i] = []
    if (len(a)%len(k) != 0):
        a += 'x' * (len(k) - len(a)%len(k))
    for i in range(len(a)):
        imp[k[i%len(k)]].append(a[i])
    print("All the keys and their respective key[int] : value[array of ints] relation - >  ",imp)
    after_sort = (dict(sorted(imp.items())))
    for i in after_sort.values():
        out += ''.join(i)
    return out


def decrypt_row_column_transposition(a:str,k:list[int])->str:
    out = ''
    imp ={}
     # 0 and 1 indexing 1 taken as 0 its fine
    for i in range(len(k)):
        imp[i-1] = []
    col_len = len(a) // len(k) # obv floor better cause 0 index start
    extra = len(a) % len(k)
    index = 0
    for i in range(len(k)):
        for j in range(col_len):
            imp[i].append(a[index])
            index += 1
        if extra > 0:
            imp[i].append(a[index])
            index += 1
            extra -= 1
    sorted_imp = dict(sorted(imp.items()))
    for i in range(col_len + 1):
        for j in (k):
            if i < len(sorted_imp[j]):# row wise huh yeh 
                out += sorted_imp[j][i]
    return out


# # Example 1
# plaintext1 = "hello"
# key1 = [3, 1, 2]
# ciphertext1 = encrypt_row_column_transposition(plaintext1, key1)
# print(ciphertext1)  # Expected output: "lhoel" (or similar, depending on key)

# decrypted1 = decrypt_row_column_transposition(ciphertext1, key1)
# print(decrypted1)  # Expected output: "hello"

# # # Example 2
# # plaintext2 = "attackatdawn"
# # key2 = [4, 3, 1, 2]
# # ciphertext2 = encrypt_row_column_transposition(plaintext2, key2)
# # print(ciphertext2)  # Expected output: "tcatakdawnat" (or similar, depending on key)

# # decrypted2 = decrypt_row_column_transposition(ciphertext2, key2)
# # print(decrypted2)  # Expected output: "attackatdawn"


# slight error in this code cant figrue it out leave it for later 