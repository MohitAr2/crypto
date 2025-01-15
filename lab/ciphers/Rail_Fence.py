import math

def encrypt_rail_fence(a:str,d:int)->str: 
    out=""
    siz = math.ceil(len(a)/d)
    #first val of mat 
    # do first index of mat first 
    # for i in range(0,siz):
    #     temp.append(a[i])
    # mat.append(temp) decrypt side logic this is 
    # if (len(a)-) edge case if not right enough size then pad it with x's 
    a = a.ljust(len(a) + len(a)%siz,'x') #parameter is ovr size 1st parm
    # print(a)
    # tmep = [] for i in range(siz,len(a)): # rem values or next row if none left then append x
    #     # print("enter",a[i],temp,mat , "exit")
    #     temp.append(a[i])
    #     # c2+=1
    #     if len(temp) == siz:
    #         mat.append(temp)
    #         temp = []
    # fence movement is 00 10 01 11 02 12 03 13
    # for i in range(0,siz):#0 1 2 .. 8 
    #     for j in range(0,d): # 0 1 ..
    #         out += mat[j][i] u did decrypt instead of encypt here 
    count = 0
    mat = []
    for i in range(d):
        mat.append([' ']*siz)
    for i in range(siz):
        for j in range(d):
            if count < len(a):
                mat[j][i] = a[count]
                count+=1
    print("Matrix rep of the given plain text in the given depth : ",mat)
    for i in mat:
        out += ''.join(i)
    return out

def decrypt_rail_fence(a:str,d:int)->str: 
    out=""
    siz = math.ceil(len(a)/d)
    count = 0
    mat = []
    for i in range(d):
        mat.append([' ']*siz)
    for i in range(d):
        for j in range(siz):
            if count < len(a):
                mat[i][j] = a[count]
                count+=1
    # fence move the vals now 
    # print(mat)
    for i in range(0,siz):#0 1 2 .. 8 
        for j in range(0,d): # 0 1 ..
            out += mat[j][i]
    return out

# # Example 1
# plaintext1 = "hello"
# depth1 = 3
# ciphertext1 = encrypt_rail_fence(plaintext1, depth1)
# print(ciphertext1)  # Expected output: "hleolx" (or similar, depending on padding)

# decrypted1 = decrypt_rail_fence(ciphertext1, depth1)
# print(decrypted1)  # Expected output: "hellox"

# # Example 2
# plaintext2 = "attackatdawn"
# depth2 = 4
# ciphertext2 = encrypt_rail_fence(plaintext2, depth2)
# print(ciphertext2)  # Expected output: "atcawtkadtxn" (or similar, depending on padding)

# decrypted2 = decrypt_rail_fence(ciphertext2, depth2)
# print(decrypted2)  # Expected output: "attackatdawn"