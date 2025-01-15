import math
import numpy as np
def encrypt_vignere(a:str,b:str): # b is the key
    #a = iajslkdja b = best loop for 
    # p[i] + k[i] mod 26 add mod size if exceeds 
    cd = "" # out str
    for i in range(0,len(a)):
        #print(ord(a[i]) , ord(b[i%len(b)]))
        c = ((ord(a[i])+(ord(b[i%len(b)]))-97)) #to maintain loop b mod len(b)
        # -97 cause 'a' starts from there 
        if c > 122:
        #this too hold the loop of a to z 
            c -= 26
        cd += chr(c)
        #print(c)
    return cd #14 lines
def encrypt_vernam(a:str,b:str):
    if(len(a)!=len(b)):
        return "Key not valid !!!" # error case
    cd =""
    c=0
    for i in range(len(a)):
        #xor 
        c = (ord(a[i])-97)^(ord(b[i])-97)
        # exceeds case 
        c += 97 # to get to the letter ascii val basically 
        cd += chr(c)
        #checked valid it is nice 
    return cd #12 lines
def encrypt_playfair(a:str,k:str)->str:
    # make metrix wrt key and so on 
    out = ""
    all = list('abcdefghiklmnopqrstuvwxyz') #rem unique i and j same taken as i 
    # print(all)
    for i in set(k): # to handle repetions in key 
        all.remove(i)
        # print(all)
    
    mat = [] # for the key 
    map_for_each_letter = {} # 'm': [0,0] , 'o' : [0,1] , ... 
    formatrix = k + ''.join(all)
    c=0
    for i in range(0,5):
        temp =[] # every 5 filled then fresh
        for j in range(0,5):
            #is a 5x5 matrix so 
            temp.append(formatrix[c])
            map_for_each_letter[formatrix[c]] = [i,j] #the pos is inserted for map 
            # is obv a vulnerability if found cause stores all data 
            c+=1
            if(j==4):
                mat.append(temp)#25 letters confirmed ? prolly
    # print(map_for_each_letter)
    # now main encryption 
    # pair them up if odd len then add filler x
    pairs = []
    if(len(a)%2==1):
        a += 'x' # extra filler char
    for i in range(0,len(a),2):
        tmep2 = [a[i],a[i+1]]
        pairs.append(tmep2)
    # print(pairs)
    # print(map_for_each_letter['a'][0])
    for i,j in pairs:
        if(map_for_each_letter[i][0]==map_for_each_letter[j][0]): # row check 
            out += mat[map_for_each_letter[i][0]][(map_for_each_letter[i][1]+1)%5] + mat[map_for_each_letter[j][0]][(map_for_each_letter[j][1]+1)%5]
        elif(map_for_each_letter[i][1]==map_for_each_letter[j][1]): # column check 
            out += mat[(map_for_each_letter[i][0]+1)%5][(map_for_each_letter[i][1])%5] + mat[(map_for_each_letter[j][0]+1)%5][(map_for_each_letter[j][1])%5]
        else:#rect case
            out += mat[map_for_each_letter[i][0]][map_for_each_letter[j][1]] + mat[map_for_each_letter[j][0]][map_for_each_letter[i][1]] # check i first or swpa the vals for order  
    return out #41 lines
def encrypt_hill(hill:str,kee:list[int])->str:
    out=""
    # based on size of k 
    oy = []
    # add remainder num of xs 
    if(len(hill)%len(kee) != 0):
        hill += 'x'*(len(hill)%len(kee))
    # def mat_mux(A,B)->list: # ensures right way input and saves space
    #     result = [[sum(a * b for a, b in zip(A_row, B_col)) 
    #                         for B_col in zip(*B)]
    #                                 for A_row in A]
    #     return result using numpy to simplify the matrix mul and inverse and adjoin and determinant stuff
    # row_len = len(k) # sqyare so column row same
    for i in range(0,len(hill),len(kee)):
        # print(i , i + len(kee))
        f = list((hill[i:i+len(kee)])) # can have a mabda here instead of extra f and g direct list 
        g = []
        for j in f:
            g.append(ord(j)-ord('a'))
        oy.append(g)
        # print(oy)
    # print(oy)
    all = []
    for i in oy:
        # print(i)
        # print(np.dot(i,kee))
        all.append((np.dot(i,kee))%26)
    # a = [12,4]
    # b = [[9,4],[5,7]]
    # print(np.dot(a,b)%26)
    # for i in range(len(all)):
    #     for j in range(len(all[i])):
    #         all[i][j] = all[i][j] % 26
    # temp = ""
    for i in all:
        for k in i: # can just use the zip part but is scalar so issues in int32 type ?
            # print(k)
            out += chr(k+97)
    # print(temp)
    #decrypt is simlar but uses det and inv from the scalar values of numpy so use that 
    return out # will do in the end
def encrypt_rail_fence(a:str,d:int)->str: # a is plain text , d is the depth of matrix
    out=""
    # max mat len of d inside has list each of len = len(a)/d first val is ceil 
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
    # temp =[]
    # for i in range(siz):
    #     temp.append(' ')
    for i in range(d):
        # temp =[]
        mat.append([' ']*siz) # imp cause if temp then 
    for i in range(siz): # have to add alternatively 
        for j in range(d):
            # print(j,i,a[count])
            if count < len(a): # to ignore the extra filler x vals 
                mat[j][i] = a[count]
                count+=1
    # print(mat)
    for i in mat:
        out += ''.join(i)
    # still cant figure the fence movement hwo to input into the matrix ? 
    return out
def encrypt_row_column_transposition(a:str,k:list[int])->str: # k is [4,3,2,1] positions permutation
    out = ""
    imp = {}
    for i in k:
        imp[i] = [] # initialize
    # ptr = k
    # lpad xs for extra vals
    if (len(a)%len(k) != 0):
        a += 'x' * (len(k) - len(a)%len(k)) # obv closest val if mid left then ? error maybe
    for i in range(len(a)):
        imp[k[i%len(k)]].append(a[i])
    after_sort = (dict(sorted(imp.items())))
    for i in after_sort.values():
        out += ''.join(i)
    # sort the map then out 
    return out
a = 'instruments'
a2 = 'atta'
playfair_key = 'monarchy'
# m = encrypt_vernam(a.lower(),b.lower())
# print(str(a))
# print(encrypt_playfair(a,b))#gatlmzclrqtx
# fdv = (encrypt_playfair(a,playfair_key)) #rssr
# print(fdv)
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

# print(decrypt_playfair(fdv,playfair_key))
depth = 2
raid = "meetmeaftertheparty" # if space can trim and ignore
# raid_out = (encrypt_rail_fence(raid,depth))
# print(raid_out)
def decrypt_rail_fence(a:str,d:int)->str: 
    out=""
    siz = math.ceil(len(a)/d)
    count = 0
    mat = []
    for i in range(d):
        mat.append([' ']*siz)
    for i in range(d):
        for j in range(siz):
            if count < len(a): # ignroes the x vals that are there !! 
                mat[i][j] = a[count]
                count+=1
    # fence move the vals now 
    # print(mat)
    for i in range(0,siz):#0 1 2 .. 8 
        for j in range(0,d): # 0 1 ..
            out += mat[j][i] #u did decrypt instead of encypt here 
    return out

# print(decrypt_rail_fence(raid_out,depth))
key = [4,3,1,2,5,6,7]
s = 'attackontitan'
# jsa = encrypt_row_column_transposition(s,key)
# print(jsa)
def decrypt_row_column_transposition(a:str,k:list[int])->str:
    out = ''
    imp ={}
     # 0 and 1 indexing 1 taken as 0 its fine 
    # K = sorted(k) 
    for i in K:
        imp[i] = []
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
        for j in k:
            if i < len(sorted_imp[j]):# row wise huh yeh 
                out += sorted_imp[j][i]
    # print(sorted_imp)
    return out
# print(decrypt_row_column_transposition(jsa,key))
# hill 
h1 = 'meetmeintheoffice'
k1 = np.array([[9,4],[5,7]]) # n x n sqyare matrix 
xdf = (encrypt_hill(h1,k1)) # works nicely done
# print(xdf)
def decrypt_hill(ciphertext: str, key: np.ndarray) -> str:
    out = ""
    n = key.shape[0] # new concept learned
    oy = []
    for i in range(0, len(ciphertext), n):
        oy.append([ord(char) - 97 for char in ciphertext[i:i+n]])
    det = int(np.round(np.linalg.det(key)))
    det_inv = pow(det, -1, 26)
    key_inv = (det_inv * np.round(det * np.linalg.inv(key)).astype(int) % 26) % 26
    # used net pre def funcs 
    all = []
    for i in oy:
        all.append(np.dot(i, key_inv) % 26)
    for i in all:
        for k in i:
            out += chr(int(k) + 97)
    return out

# print(decrypt_hill(xdf,k1))
# print("Enter your key as a matrix input format [] = ")
# n = int(input("Size of matrix input  [sqaure matrix] so 2 if 2x2 matrix ... = "))
# K = []
# for i in range(n):
#     temp = []
#     for j in range(n):
#         hh = int(input(f"at index {i,j} : "))
#         temp.append(hh)
#     K.append(temp)
# print(K)

# string_list = "[1, 2, 3, 'hello']"
# my_list = eval(string_list)
# print(my_list)
def encrypt_play(a:str,k:str):
    # make the matrix first 
    # 5x5 matrix        
    temp = []
    ovr = []
    all1 = list('abcdefghiklmnopqrstuvwxyz')  # i and j same ignore j exsistence
    for i in range(0,len(k)):
        if ( k[i] == 'j'):
            k[i] = 'i'                
        all1.remove(k[i])
    #map for all chars used 
    for i in k+(''.join(all1)): # key doesnt have reppeated letters 
        if (len(temp)) < 5:
            temp.append(i)
            print(temp)
        else:
            # insert into main ovr
            ovr.append(temp)
            temp = []
            temp.append(i)  #next line basically
            # print(temp)
    # return ovr
    #got the matrix 
    if(len(a)%2 == 1):
        #odd size then append x to end 
        a+='x' # filler letter only to end 
        
        # can add rule of the in between later 
    #  club them 
    out=""
    a_match_vals =[]
    # pos in mat req each time convert a to set 
    t1 =[]
    t2 =[]
    for i in range(0,len(a)):
        for j in range(0,5):
            for k in range(0,5):
                if(a[i] == ovr[j][k]):
                    if (len(t1) == len(t2) == 2): # filled both then
                        if(t1[0] == t2[0]):
                            a_match_vals.append('r')#row
                        elif(t1[1]==t2[1]):
                            a_match_vals.append('c')#column
                        else:
                            a_match_vals.append('n') # n menas none so rect
                        t1.clear()
                        t2.clear()
                    if(len(t2) == 0):
                        t1 = [i,j]
                    else:
                        t2 = [i,j]
                    # a_pos_vals.append([t1,t2]) #combine 2 letters together and give conditions here itself 
    print(a_match_vals)
    # for i,j in a_pos_vals:
    #     if()

def encrypt_caesar(a:str,k)->str:
        b = ""
        l = 0
        for i in range(0,len(a)):
                # l = ord((a[i])) + k
                l = (ord(a[i]))
                l = (l + k)
                # if(l > z val then -= 26)
                if(l > 122):
                        l = l - 26
                b += chr(l)
        return b

