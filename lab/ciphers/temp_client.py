import socket 

def F(A:str)->str: # helper function for Exansion to 8 bits
        f_map = [4,1,2,3,2,3,4,1]
        out = ''
        for i in f_map:
            out += A[i-1]
        return out

def bn_to_dec(a:str)->int: # used in the substitution box 
        if a == '00':
            return 0
        elif a == '01':
            return 1
        elif a == '10':
            return 2
        else:
            return 3
        
def dec_to_bin(a:int)->str: # used in the substitution box 
        if a == 0:
            return '00'
        elif a == 1:
            return '01'
        elif a == 2:
            return '10'
        elif a == 3:
            return '11'
        
def fk(L:str,R:str,key1_or2:str)->str: # 2 times we use this func cause 2 rounds in S-DES
        # fk(L,R) = L xor F(R,key1_or2) + R concat
        x = F(R) # generalized R here is R0 and R1 given input
        # print(f"After Expansion : {x}")
        # now xor 
        nu = ''
        for i in range(len(key1_or2)):
            nu += str(int(x[i])^int(key1_or2[i])) 
            # 0 or 1 taken as int vals fro xor gate operatin bitwise
        nu_1 = nu[:4]
        nu_2 = nu[4:]
        # print(f'After XOR : {nu_1} {nu_2}') # to represent left half and right half 
        # substituion steps 
        S_box_1 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]] # S1 matrix
        S_box_2 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]] # S2 matrix
        # nu_1 to sub_box_1
        
        nu_1_fir_las = nu_1[0] + nu_1[3] # first and last bit is the row value for S1
        nu_1_mid = nu_1[1] + nu_1[2] # middle two are for the column value for for S1

        # nu_2 to sub_box_2

        nu_2_fir_las =  nu_2[0] + nu_2[3] # first and last bit is the row value for S2
        nu_2_mid = nu_2[1] + nu_2[2] # middle two are for the column value for for S2
        
        # 2 bit output after sub box call for each of them 

        nu_1_out = dec_to_bin(S_box_1[bn_to_dec(nu_1_fir_las)][bn_to_dec(nu_1_mid)])
        nu_2_out = dec_to_bin(S_box_2[bn_to_dec(nu_2_fir_las)][bn_to_dec(nu_2_mid)])

        # print(f'The result of sub boxes combined : {nu_1_out} {nu_2_out}')

        for_p4 = nu_1_out+nu_2_out # combine them 

        P4 = [2,4,3,1]
        p4 = ''
        for i in P4:
            p4 += for_p4[i-1]
        
        return p4 # retunrs after the permutation 4 bit output



def encrypt_simp_des(plain:str,kee:str)->str:
    # 2 sub keys genrate first 
    P10 = [3,5,2,7,4,10,1,9,8,6] # positions to permutate into 
    p10 = ''
    for i in P10:
        p10 += kee[i-1] # indexing from 
    # print(f"Step P10 : {p10}")
    # split to two hals 
    pfirst = p10[:5]
    psecond = p10[5:]
    # print(f"Split them\n {pfirst} {psecond}")
    # separate LCS times one
    pfirst_afterlcs = pfirst[1:] + pfirst[0]
    psecond_afterlcs = psecond[1:] + psecond[0]
    # print(f"After LCS x 1 : {pfirst_afterlcs} {psecond_afterlcs}")
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
    # print(f"For k2 now after left circular shift two more times to already shifted halves : {p2_afterlcs_1} {p2_afterlcs_2}")
    k2 = ''
    for_p8_part_2 = p2_afterlcs_1 + p2_afterlcs_2 # combine for P8 
    for i in P8:
        k2 += for_p8_part_2[i-1]
    print(f"Key 2 : {k2}")


    # S-DES main

    # IP part initial permutation for the plain text 
    IP = [2,6,3,1,4,8,5,7]
    pt_IP = ''
    for i in IP:
        pt_IP += plain[i-1] # indexing from 1 given so 
    print(f'IP : {pt_IP}')
    # round 1 begins 
    
    L0 = pt_IP[:4] # left most 4 bits
    R0 = pt_IP[4:] # Right half 4 bits
    print("Round 1 begins : ")
    r1_out = fk(L0,R0,k1)
    print(f'output of round 1 : {L0} {r1_out}')
    # r1 ends
    L1 = R0 # space waste but okay
    R1 = ''
    # for r1 we xor l0 and r1_out 
    for i in range(len(r1_out)):
        R1 += str(int(L0[i]) ^ int(r1_out[i]))
    # round 2 time
    print('Round 2 begins ')
    # print(f'now for round 2 we get the L1 : {L1} and R1 : {R1}')
    r2_out = fk(L1,R1,k2) # this time around we send key 2 as input for the xor layer
    print(f'output of round 2 : {L1} {r2_out}')
    final_ip_inv_input = '' # first half we fill 
    for i in range(len(r2_out)):
        final_ip_inv_input += str(int(L1[i]) ^ int(r2_out[i])) 
    final_ip_inv_input += R1 # right half now we append
    # print(f'The cipher before applying IP_inverse : {final_ip_inv_input}')

    # for IP-1 in the end inverse permutation 

    IP_inv = [4,1,3,5,7,2,8,6]
    cipher_text = ''
    for i in IP_inv:
        cipher_text += final_ip_inv_input[i-1]
    # print(f'The cipher text sent : {cipher_text}')
    return cipher_text

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8080))
    print("Connected to the server\n\n")
    while True:
        mess = str(input("Plain text 8 bit length binary string input only : ")) #10100101
        k = str(input("Key in binary format 10 bits : ")) #1101010010
        message = encrypt_simp_des(mess,k)
        client_socket.send(k.encode('utf-8'))
        print(f"Encrypted_message of {mess} is : {message}")#11010101
        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

if __name__ == "__main__":
    start_client()