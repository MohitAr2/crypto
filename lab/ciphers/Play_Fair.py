def encrypt_playfair(a:str,k:str)->str:
    out = ""
    all = list('abcdefghiklmnopqrstuvwxyz') #rem unique i and j same taken as i 
    for i in set(k): # to handle repetions in key 
        all.remove(i)
    mat = [] # for the key 
    map_for_each_letter = {} # 'm': [0,0] , 'o' : [0,1] , ... 
    formatrix = k + ''.join(all)
    c=0
    for i in range(0,5):
        temp =[]
        for j in range(0,5):
            temp.append(formatrix[c])
            map_for_each_letter[formatrix[c]] = [i,j]
            c+=1
            if(j==4):
                mat.append(temp)
    pairs = []
    if(len(a)%2==1):
        a += 'x' # extra filler char taken as x 
    for i in range(0,len(a),2):
        tmep2 = [a[i],a[i+1]]
        pairs.append(tmep2)
    for i,j in pairs:
        if(map_for_each_letter[i][0]==map_for_each_letter[j][0]): # row check 
            out += mat[map_for_each_letter[i][0]][(map_for_each_letter[i][1]+1)%5] + mat[map_for_each_letter[j][0]][(map_for_each_letter[j][1]+1)%5]
        elif(map_for_each_letter[i][1]==map_for_each_letter[j][1]): # column check 
            out += mat[(map_for_each_letter[i][0]+1)%5][(map_for_each_letter[i][1])%5] + mat[(map_for_each_letter[j][0]+1)%5][(map_for_each_letter[j][1])%5]
        else:#rect case
            out += mat[map_for_each_letter[i][0]][map_for_each_letter[j][1]] + mat[map_for_each_letter[j][0]][map_for_each_letter[i][1]] # check i first or swpa the vals for order  
    return out

def decrypt_playfair(a:str,k:str)->str:
    out = ""
    all = list('abcdefghiklmnopqrstuvwxyz') #rem unique i and j same taken as i 
    for i in set(k): # to handle repetions in key 
        all.remove(i)
    mat = [] # for the key 
    map_for_each_letter = {} # 'm': [0,0] , 'o' : [0,1] , ... 
    formatrix = k + ''.join(all)
    c=0
    for i in range(0,5):
        temp =[]
        for j in range(0,5):
            temp.append(formatrix[c])
            map_for_each_letter[formatrix[c]] = [i,j]
            c+=1
            if(j==4):
                mat.append(temp)
    pairs = []
    if(len(a)%2==1):
        a += 'x' # extra filler char taken as x 
    for i in range(0,len(a),2):
        tmep2 = [a[i],a[i+1]]
        pairs.append(tmep2)
    for i,j in pairs:
        if(map_for_each_letter[i][0]==map_for_each_letter[j][0]): # row check 
            out += mat[map_for_each_letter[i][0]][(map_for_each_letter[i][1]-1)%5] + mat[map_for_each_letter[j][0]][(map_for_each_letter[j][1]-1)%5]
        elif(map_for_each_letter[i][1]==map_for_each_letter[j][1]): # column check only -1 instead of +1 obv 
            out += mat[(map_for_each_letter[i][0]-1)%5][(map_for_each_letter[i][1])%5] + mat[(map_for_each_letter[j][0]-1)%5][(map_for_each_letter[j][1])%5]
        else:#rect case no change in both 
            out += mat[map_for_each_letter[i][0]][map_for_each_letter[j][1]] + mat[map_for_each_letter[j][0]][map_for_each_letter[i][1]] # check i first or swpa the vals for order  
    return out 

# Example 1
# plaintext1 = "hello"
# key1 = "keyword"
# ciphertext1 = encrypt_playfair(plaintext1, key1)
# print(ciphertext1)  # Expected output: "hidiyx" (or similar, depending on padding)

# decrypted1 = decrypt_playfair(ciphertext1, key1)
# print(decrypted1)  # Expected output: "hellox"

# # Example 2
# plaintext2 = "attackatdawn"
# key2 = "playfair"
# ciphertext2 = encrypt_playfair(plaintext2, key2)
# print(ciphertext2)  # Expected output: "pmbbqmbqmbqz" (or similar, depending on padding)

# decrypted2 = decrypt_playfair(ciphertext2, key2)
# print(decrypted2)  # Expected output: "attackatdawn"