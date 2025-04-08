def power_mod(a:int,b:int,m:int)->int:
    val = 1
    if(a>m):
        a = a%m
    if(a==1):
        return 1
    if(m == 1):
        return a
    if(a == 0):
        return 0
    b_bin_form = []
    pwoer_vals = {}
    bit = 1
    while(b!=0):
        r = b%2
        b_bin_form.append(r)
        pwoer_vals[bit] = -1 # initialiuze them all
        bit += 1
        b //= 2
    # print(b_bin_form)
    pwoer_vals[1] = a
    st = 2
    while(st < bit):
        # print('6^',st,6**st % m)
        pwoer_vals[st] =  pwoer_vals[st-1]*pwoer_vals[st-1] % m # keep squaring the vals      
        st+=1
    # print(pwoer_vals)
    for i in range(bit-1):
        if(b_bin_form[i]==1):
            val *= pwoer_vals[i+1] 
    return val % m


# print(power_mod(7,15,71))
# # print(power_mod(19,56,71))
# # print(power_mod(25*26,1,71))



def gen_keys():
    kee = '1010000010'
    P10 = [3,5,2,7,4,10,1,9,8,6]
    P8 = [6,3,7,4,8,5,10,9] # given bit postiotns
    p10 = ''
    for i in P10:
        p10 += kee[i-1] # indexing from 
    print(f"Step P10 : {p10}")
    # split to two hals 
    pfirst = p10[:5]
    psecond = p10[5:]
    print(f"Split them\n {pfirst} {psecond}")
    # separate LCS times one
    pfirst_afterlcs = pfirst[1:] + pfirst[0]
    psecond_afterlcs = psecond[1:] + psecond[0]
    print(f"After LCS x 1 : {pfirst_afterlcs} {psecond_afterlcs}")
    P8 = [6,3,7,4,8,5,10,9] # given bit postiotns
    k1 = ''
    for_p8 = pfirst_afterlcs+psecond_afterlcs # combine for P8 
    for i in P8:
        k1 += for_p8[i-1]
    print(f"Key 1 : {k1}")
    # for k2 2 x LCS or 1 more lcs on pfirst and psecond
    p2_afterlcs_1 = pfirst_afterlcs[2:] + pfirst_afterlcs[:2] # done 2 times to the pfirst_afterlcs
    p2_afterlcs_2 = psecond_afterlcs[2:] + psecond_afterlcs[:2] # swap the 2 bits obv cause 4 bit 
    # apply P8 again 
    print(f"For k2 now after left circular shift two more times to already shifted halves : {p2_afterlcs_1} {p2_afterlcs_2}")
    k2 = ''
    for_p8_part_2 = p2_afterlcs_1 + p2_afterlcs_2 # combine for P8 
    for i in P8:
        k2 += for_p8_part_2[i-1]
    print(f"Key 2 : {k2}")

gen_keys()