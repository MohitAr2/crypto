def encrypt_simp_des(plain:str,kee:str)->str:
    # 2 sub keys genrate first 
    P10 = [3,5,2,7,4,10,1,9,8,6] # positions to permutate into 
    p10 = ''
    for i in P10:
        p10 += kee[i-1] # indexing from 
    # split to two hals 
    pfirst = p10[:5]
    psecond = p10[5:]
    # separate LCS times one
    pfirst_afterlcs = pfirst[1:] + pfirst[0]
    psecond_afterlcs = psecond[1:] + psecond[0]
    P8 = [6,3,7,4,8,5,10,9] # given bit postiotns
    k1 = ''
    for_p8 = pfirst_afterlcs+psecond_afterlcs
    for i in P8:
        k1 += for_p8[i-1]
    print("Key 1 : ",k1)
    # for k2 2 x LCS or 1 more lcs on pfirst and psecond
    p2_afterlcs_1 = pfirst_afterlcs[1:] + pfirst_afterlcs[0]
    p2_afterlcs_2 = psecond_afterlcs[1:] + psecond_afterlcs[0]
    # apply P8 again 
    k2 = ''
    for_p8_part_2 = p2_afterlcs_1 + p2_afterlcs_2
    for i in P8:
        k2 += for_p8_part_2[i-1]
    print("Key 2 : ",k2)

    # S-DES main

    # IP part initial permutation
    IP = [2,6,3,1,4,8,5,7]
    pt_IP = ''
    for i in IP:
        pt_IP += plain[i-1]
    # 
    L0 = pt_IP[:4] # left most bits
    R0 = pt_IP[4:]
    def F(A:str)->str:
        f_map = [4,1,2,3,2,3,4,1]
        out = ''
        for i in f_map:
            out += A[i-1]
        return out
    def bn_to_dec(a:str)->int:
        if a == '00':
            return 0
        elif a == '01':
            return 1
        elif a == '10':
            return 2
        else:
            return 3
    def dec_to_bin(a:int)->str:
        if a == 0:
            return '00'
        elif a == 1:
            return '01'
        elif a == 2:
            return '10'
        elif a == 3:
            return '11'
    def fk(L:str,R:str,key1_or2:str)->str: # 2 times we use this so 
        # fk(L,R) = L xor F(R,key1_or2) + R concat
        x = F(R)
        # now xor 
        nu = ''
        for i in range(len(key1_or2)):
            nu += str(int(x[i])^int(key1_or2[i]))  # 0 or 1 taken as int vals fro xor gate operatin bitwise
        print('After XOR : ',nu[:4],' ',nu[4:]) # to represent
        nu_1 = nu[:4]
        nu_2 = nu[4:]
        S_box_1 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
        S_box_2 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
        # nu_1 to sub_box_1
        nu_1_fir_las = nu_1[0] + nu_1[3]
        nu_1_mid = nu_1[1] + nu_1[2]
        nu_2_fir_las =  nu_2[0] + nu_2[3]
        nu_2_mid = nu_2[1] + nu_2[2]
        # 2 bit output after sub box 
        nu_1_out = dec_to_bin(S_box_1[bn_to_dec(nu_1_fir_las)][bn_to_dec(nu_1_mid)])
        nu_2_out = dec_to_bin(S_box_2[bn_to_dec(nu_2_fir_las)][bn_to_dec(nu_2_mid)])
        for_p4 = nu_1_out+nu_2_out # combine them 
        P4 = [2,4,3,1]
        p4 = ''
        for i in P4:
            p4 += for_p4[i-1]
        return p4
    r1_out = fk(L0,R0,k1)
    # r1 ends
    L1 = R0
    R1 = ''
    # for r1 we xor l0 and r1_out 
    for i in range(len(r1_out)):
        R1 += str(int(L0[i]) ^ int(r1_out[i]))
    # round 2 time
    

    # for IP-1 in the end inverse permutation 
    IP_inv = [4,1,3,5,7,2,8,6]



    return ""

pt = ''
ker = ''

print(encrypt_simp_des(pt,ker))