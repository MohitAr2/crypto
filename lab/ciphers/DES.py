def generate_keys(key:str)->list[str]:
    # 64 bit key 
    # removes parity
    keys_list = []
    keyperm_56 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
    # round wise bit shifts on prev val 
    shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]
    # each putput round key is 48 bit so we reduce 
    key_comp = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
    def lcl(bit_str_28:str,round_times:int):
        # once lcl always 
        out = bit_str_28[1:]+bit_str_28[0]
        if(round_times == 1):
            return out
        else:
            out2 = out[1:] + out[0]
            return  out2
    key_56 = ""
    for i in keyperm_56:
        key_56 += key[i-1]
    for rounds in range(0,16):# 16 rounds
        key_left = key_56[:28]
        key_right = key_56[28:]
        key_56 = lcl(key_left,shift_table[rounds]) +  lcl(key_right,shift_table[rounds])# use the shift array for 16 rounds 
        ki = ''
        for i in key_comp:
            ki += key_56[i-1]
        keys_list.append(ki) # for each round

    return keys_list

def encrypt_DES(pt_in:str,k_in:str,flag:bool)->str:
    def bin2hex(s):
        mp = {"0000": '0',
            "0001": '1',
            "0010": '2',
            "0011": '3',
            "0100": '4',
            "0101": '5',
            "0110": '6',
            "0111": '7',
            "1000": '8',
            "1001": '9',
            "1010": 'A',
            "1011": 'B',
            "1100": 'C',
            "1101": 'D',
            "1110": 'E',
            "1111": 'F'}
        hex = ""
        for i in range(0, len(s), 4):
            ch = ""
            ch = ch + s[i]
            ch = ch + s[i + 1]
            ch = ch + s[i + 2]
            ch = ch + s[i + 3]
            hex = hex + mp[ch]
    
        return hex
    def hex2bin(s):
        mp = {'0': "0000",
            '1': "0001",
            '2': "0010",
            '3': "0011",
            '4': "0100",
            '5': "0101",
            '6': "0110",
            '7': "0111",
            '8': "1000",
            '9': "1001",
            'A': "1010",
            'B': "1011",
            'C': "1100",
            'D': "1101",
            'E': "1110",
            'F': "1111"}
        bin = ""
        for i in range(len(s)):
            bin = bin + mp[s[i]]
        return bin
        
    # as input of pt is not binary but in hexa so and key too so we convert them both 
    pt = hex2bin(pt_in) 
    k = hex2bin(k_in) 

    # Initial Permutation Table
    initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                    60, 52, 44, 36, 28, 20, 12, 4,
                    62, 54, 46, 38, 30, 22, 14, 6,
                    64, 56, 48, 40, 32, 24, 16, 8,
                    57, 49, 41, 33, 25, 17, 9, 1,
                    59, 51, 43, 35, 27, 19, 11, 3,
                    61, 53, 45, 37, 29, 21, 13, 5,
                    63, 55, 47, 39, 31, 23, 15, 7]
    
    ct = ''
    for i in initial_perm:
        ct += pt[i-1]

    print('After IP round : ',bin2hex(ct))
    all_round_keys = generate_keys(k)
    if flag:
        all_round_keys = all_round_keys[::-1]
        # reverse for decrypt obv
    # for each round now 
    def xor(a:str,b:str)->str:
        if(a!=b):
            return "1"
        else:
            return "0"
    # Binary to decimal conversion
    def bin2dec(binary):
        binary = int(binary)
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return decimal
    
    # Decimal to binary conversion   
    def dec2bin(num):
        res = bin(num).replace("0b", "")
        if(len(res) % 4 != 0):
            div = len(res) / 4
            div = int(div)
            counter = (4 * (div + 1)) - len(res)
            for i in range(0, counter):
                res = '0' + res
        return res
     # s-box time
    sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
        # Expansion D-box Table
    exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
         6, 7, 8, 9, 8, 9, 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1]
        # Straight Permutation Table
    per = [16,  7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2,  8, 24, 14,
       32, 27,  3,  9,
       19, 13, 30,  6,
       22, 11,  4, 25]
    # print(all_round_keys)
    for rounds in range(0,16):          
        L0 = ct[:32]
        R0 = ct[32:]
        # exapnsion of right half only 
        R_in =''
        ptr = 0
        for i in exp_d:
            R_in += xor(R0[i-1],all_round_keys[rounds][ptr])# round - 1 for the key 
            # bitwise we do xor 
            ptr+=1
            # print(ptr,R_in)
        # split into 6 parts the 48 bit val so 6 len each 
        s_box_temp = ''
        for parts in range(0,8):
            value = R_in[parts*6:parts*6+6]
            r = bin2dec(str(value[0]+value[-1]))
            c = bin2dec(value[1:-1])
            curr_s_box = sbox[parts]

            temps = dec2bin(curr_s_box[r][c])
            # if(len(temps)<4):
            #     temps = "0"*(4-len(temps))+temps # padding
            # print(temps)
            s_box_temp +=  temps # have to pad for 4 hexas 
            # stull size is 32 here 
        R_next = ''
        # print(s_box_temp)
        ptr = 0
        for jk in per:
            R_next += xor(s_box_temp[jk-1],L0[ptr])
            ptr+=1
        L_next = R0
        ct = L_next+R_next
        print(f'Round {rounds+1} HEX: ',bin2hex(ct))

    # after 16 rounds only 2 more things to do 

    ct = ct[32:]+ct[:32] # check if this is fine in pyhton should work casue new obj is made here too
    # Final Permutation Table
    ct_out = ''
    final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]
    for another in final_perm:
        ct_out += ct[another-1]

    return bin2hex(ct_out)


def decrypt_DES(ct:str,k:str)->str:
    # all_round_keys = generate_keys(k)[::-1] # apprently in rev right cause symm algo 
    pt = encrypt_DES(ct,k,flag=True)
    return pt



# plain_t = "123456ABCD132536"
# key_sent = "AABB09182736CCDD"
# cipher = encrypt_DES(plain_t,key_sent,False)
# print('ciper is :', cipher)
# pt_out = decrypt_DES(cipher,key_sent)

# if(pt_out == plain_t):
#     print('ok')
# else:
#     print('no')