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
            'a': "1010",
            'b': "1011",
            'c': "1100",
            'd': "1101",
            'e': "1110",
            'f': "1111"}
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i].lower()]
    return bin

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
            "1010": 'a',
            "1011": 'b',
            "1100": 'c',
            "1101": 'd',
            "1110": 'e',
            "1111": 'f'}
        hex = ""
        for i in range(0, len(s), 4):
            ch = ""
            ch = ch + s[i]
            ch = ch + s[i + 1]
            ch = ch + s[i + 2]
            ch = ch + s[i + 3]
            hex = hex + mp[ch]
    
        return hex
def xor(a:chr,b:chr):
    if(a==b):
        return '0'
    else:
        return '1'
    
def LCL(hh:str)->str:
    return hh[2:]+hh[0]+hh[1]

def S_box(input_word:str):
    S_BOX = (
   0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
   0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
   0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
   0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
   0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
   0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
   0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
   0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
   0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
   0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
   0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
   0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
   0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
   0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
   0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
   0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
)
        
    input_word_int = int(input_word, 16)
    input_bytes = [(input_word_int >> (8 * i)) & 0xFF for i in range(4)][::-1]
    substituted_bytes = [S_BOX[byte] for byte in input_bytes]
    binary_str = ''.join(format(byte, '08b') for byte in substituted_bytes)

    return binary_str


def generate_keys(k:str,rounds:int): 
    round_const ={1:'01',2:'02',3:'04',4:'08',5:'10',6:'20',7:'40',8:'80',9:'1b',10:'36',11:'00',12:'00',13:'00',14:'00',15:'00'}

    w0 = k[:8]
    w1 = k[8:16]
    w2 = k[16:24]
    w3 = k[24:32]
    all_keys = [w0,w1,w2,w3]
    temp = ''
    ptr = 0
    for i in range(4,(rounds+1)*4):
        temp = ''
        if(i%4!=0):
            first_val = hex2bin(all_keys[i-1]) 
            last_val = hex2bin(all_keys[i-4])
            for i in range(len(w0)*4):
                temp += xor(first_val[i],last_val[i])
        else:
            ptr+=1 
            first_val = hex2bin(all_keys[i-4])
            inner_val = S_box(LCL(all_keys[i-1]))
            round_bin_val = hex2bin(round_const[ptr]) 

            for i in range(8):# first 8 vals then 
                temp += xor(xor(first_val[i],inner_val[i]),round_bin_val[i])

            for i in range(8,32):
                temp += xor(first_val[i],inner_val[i])
            
        all_keys.append(bin2hex(temp))
    return all_keys


def convert_32hex_to_byte_array(val:str):
    mat_pt = []
    temp = []
    for i in range(0,4):
        temp=[]
        ti = 4
        j = i*2
        while(ti!=0):
            temp.append(val[j:j+2])
            # print(j,j+2)
            j+=8
            ti-=1
        mat_pt.append(temp)
    return mat_pt
def convert_byte_array_to_hex(X):
    hex_str = ''
    for i in range(4):
        for j in range(4):
            hex_str += X[j][i]
    return hex_str
def mat_xor(mat1,mat2):
    after = []
        # tempo_round =[]
    for i in range(0,4):
        tempo_round =[]
        for j in range(0,4):
            temp_st =''
            val1 = hex2bin(mat1[i][j])
            val2 = hex2bin(mat2[i][j])
            for k in range(8): # 1 byte per 
                temp_st += xor(val1[k],val2[k])
            tempo_round.append(bin2hex(temp_st))
        after.append(tempo_round)
    return after
def xor2(a1:str,a2:str):
    fin =''
    for i in range(8):
        fin += xor(a1[i],a2[i])
    return fin

def dot_mux(con: str, val: str) -> str:
    val_bin = hex2bin(val)

    if con == '01':
        return val_bin
    elif con == '02':
        return val_bin[1:] + '0' if val_bin[0] == '0' else xor2(val_bin[1:] + '0', hex2bin('1b'))
    elif con == '03':
        return xor2(val_bin, dot_mux('02', val))
    elif con == '09':
        return xor2(dot_mux('08', val), val_bin)
    elif con == '0b':
        return xor2(dot_mux('09', val), dot_mux('02', val))
    elif con == '0d':
        return xor2(dot_mux('09', val), dot_mux('04', val))
    elif con == '0e':
        return xor2(dot_mux('0c', val), dot_mux('02', val))
    elif con == '04':
        return dot_mux('02', dot_mux('02', val))
    elif con == '08':
        return dot_mux('04', dot_mux('02', val))
    elif con == '0c':
        return xor2(dot_mux('08', val), dot_mux('04', val))
 

def encrypt_AES(PT:str,KE:str):
    ke = KE.lower()
    pt = PT.lower()
    ct =''
   
    plain_text_matrix = convert_32hex_to_byte_array(pt)
    
    print('Initial plaintext [state matrix]: ',plain_text_matrix)
    print('HEX format : ',convert_byte_array_to_hex(plain_text_matrix))
    print('\n\n')
    mat_round_key = [] 

    rounds = {32:10,48:12,64:15}

    keys_for = generate_keys(ke,rounds[len(ke)]) 

    # works yeh 10 rounds only valid for now dont know the val of round const after r10
    
    after_ri = mat_xor(plain_text_matrix,convert_32hex_to_byte_array(''.join(keys_for[:4])))

    print('Round 0 : ',after_ri)
    print('HEX format : ',convert_byte_array_to_hex(after_ri))
    print('\n\n')

    Sub_box = {
    '00': {'00': '63', '01': '7c', '02': '77', '03': '7b', '04': 'f2', '05': '6b', '06': '6f', '07': 'c5', '08': '30', '09': '01', '0a': '67', '0b': '2b', '0c': 'fe', '0d': 'd7', '0e': 'ab', '0f': '76'},
    '10': {'00': 'ca', '01': '82', '02': 'c9', '03': '7d', '04': 'fa', '05': '59', '06': '47', '07': 'f0', '08': 'ad', '09': 'd4', '0a': 'a2', '0b': 'af', '0c': '9c', '0d': 'a4', '0e': '72', '0f': 'c0'},
    '20': {'00': 'b7', '01': 'fd', '02': '93', '03': '26', '04': '36', '05': '3f', '06': 'f7', '07': 'cc', '08': '34', '09': 'a5', '0a': 'e5', '0b': 'f1', '0c': '71', '0d': 'd8', '0e': '31', '0f': '15'},
    '30': {'00': '04', '01': 'c7', '02': '23', '03': 'c3', '04': '18', '05': '96', '06': '05', '07': '9a', '08': '07', '09': '12', '0a': '80', '0b': 'e2', '0c': 'eb', '0d': '27', '0e': 'b2', '0f': '75'},
    '40': {'00': '09', '01': '83', '02': '2c', '03': '1a', '04': '1b', '05': '6e', '06': '5a', '07': 'a0', '08': '52', '09': '3b', '0a': 'd6', '0b': 'b3', '0c': '29', '0d': 'e3', '0e': '2f', '0f': '84'},
    '50': {'00': '53', '01': 'd1', '02': '00', '03': 'ed', '04': '20', '05': 'fc', '06': 'b1', '07': '5b', '08': '6a', '09': 'cb', '0a': 'be', '0b': '39', '0c': '4a', '0d': '4c', '0e': '58', '0f': 'cf'},
    '60': {'00': 'd0', '01': 'ef', '02': 'aa', '03': 'fb', '04': '43', '05': '4d', '06': '33', '07': '85', '08': '45', '09': 'f9', '0a': '02', '0b': '7f', '0c': '50', '0d': '3c', '0e': '9f', '0f': 'a8'},
    '70': {'00': '51', '01': 'a3', '02': '40', '03': '8f', '04': '92', '05': '9d', '06': '38', '07': 'f5', '08': 'bc', '09': 'b6', '0a': 'da', '0b': '21', '0c': '10', '0d': 'ff', '0e': 'f3', '0f': 'd2'},
    '80': {'00': 'cd', '01': '0c', '02': '13', '03': 'ec', '04': '5f', '05': '97', '06': '44', '07': '17', '08': 'c4', '09': 'a7', '0a': '7e', '0b': '3d', '0c': '64', '0d': '5d', '0e': '19', '0f': '73'},
    '90': {'00': '60', '01': '81', '02': '4f', '03': 'dc', '04': '22', '05': '2a', '06': '90', '07': '88', '08': '46', '09': 'ee', '0a': 'b8', '0b': '14', '0c': 'de', '0d': '5e', '0e': '0b', '0f': 'db'},
    'a0': {'00': 'e0', '01': '32', '02': '3a', '03': '0a', '04': '49', '05': '06', '06': '24', '07': '5c', '08': 'c2', '09': 'd3', '0a': 'ac', '0b': '62', '0c': '91', '0d': '95', '0e': 'e4', '0f': '79'},
    'b0': {'00': 'e7', '01': 'c8', '02': '37', '03': '6d', '04': '8d', '05': 'd5', '06': '4e', '07': 'a9', '08': '6c', '09': '56', '0a': 'f4', '0b': 'ea', '0c': '65', '0d': '7a', '0e': 'ae', '0f': '08'},
    'c0': {'00': 'ba', '01': '78', '02': '25', '03': '2e', '04': '1c', '05': 'a6', '06': 'b4', '07': 'c6', '08': 'e8', '09': 'dd', '0a': '74', '0b': '1f', '0c': '4b', '0d': 'bd', '0e': '8b', '0f': '8a'},
    'd0': {'00': '70', '01': '3e', '02': 'b5', '03': '66', '04': '48', '05': '03', '06': 'f6', '07': '0e', '08': '61', '09': '35', '0a': '57', '0b': 'b9', '0c': '86', '0d': 'c1', '0e': '1d', '0f': '9e'},
    'e0': {'00': 'e1', '01': 'f8', '02': '98', '03': '11', '04': '69', '05': 'd9', '06': '8e', '07': '94', '08': '9b', '09': '1e', '0a': '87', '0b': 'e9', '0c': 'ce', '0d': '55', '0e': '28', '0f': 'df'},
    'f0': {'00': '8c', '01': 'a1', '02': '89', '03': '0d', '04': 'bf', '05': 'e6', '06': '42', '07': '68', '08': '41', '09': '99', '0a': '2d', '0b': '0f', '0c': 'b0', '0d': '54', '0e': 'bb', '0f': '16'}
}
    

    index_rounds_words = 0
    for rounds_here in range(0,rounds[len(ke)]): 
        index_rounds_words += 4
        # number of rounds is based on the key size 
        # sbox step we need the '00' to be taken as ['00']['00'] lpad the 0 to both the r and c
        fin_per_round =[]
        for i in range(4):
            tempor_per_r = []
            for j in range(4):
                tempor_per_r.append(Sub_box[after_ri[i][j][0]+'0']['0'+after_ri[i][j][1]]) # if deosnt add str inside then set vals
            fin_per_round.append(tempor_per_r)

        temp1 = fin_per_round[1][0]
        fin_per_round[1][0] = fin_per_round[1][1]
        fin_per_round[1][1] = fin_per_round[1][2]
        fin_per_round[1][2] = fin_per_round[1][3]
        fin_per_round[1][3] = temp1

        fin_per_round[2][0],fin_per_round[2][2] = fin_per_round[2][2],fin_per_round[2][0]
        fin_per_round[2][3],fin_per_round[2][1] = fin_per_round[2][1],fin_per_round[2][3]

        temp2 = fin_per_round[3][3] 
        fin_per_round[3][3] = fin_per_round[3][2]
        fin_per_round[3][2] = fin_per_round[3][1]
        fin_per_round[3][1] = fin_per_round[3][0]
        fin_per_round[3][0] = temp2 

        fixed_mix_col =[
        ['02', '03', '01', '01'],
        ['01', '02', '03', '01'],
        ['01', '01', '02', '03'],
        ['03', '01', '01', '02']
        ]

        if(rounds_here < rounds[len(ke)]-1):
            out_mix_col = [
                        ['00','00','00','00'],
                        ['00','00','00','00'],
                        ['00','00','00','00'],
                        ['00','00','00','00']
                        ]
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        temperer =''
                        dot_mux_val_op = dot_mux(fixed_mix_col[i][k],fin_per_round[k][j])
                        bin_out_mix_col = hex2bin(out_mix_col[i][j])
                        for m in range(8):# bit wise xor so 
                            temperer += xor(bin_out_mix_col[m],dot_mux_val_op[m])
                        out_mix_col[i][j] = bin2hex(temperer)
        else: # last round no mix col
            out_mix_col = fin_per_round

        mat_round_key = convert_32hex_to_byte_array(''.join(keys_for[index_rounds_words:index_rounds_words+4]))
        print('impppppp ppppp ',mat_round_key)
        after_ri = mat_xor(mat_round_key,out_mix_col)

        print(f'after Round {rounds_here+1} transform : ',after_ri)
        print('HEX format : ',convert_byte_array_to_hex(after_ri))
        print('\n\n')

    for i in range(4):
        for j in range(4):
            ct += after_ri[j][i]
        # final transpose return
    return ct

def inv_shift_rows(state):
    # shift right by 1 2 3 
    temp1 = state[1][3]
    state[1][1] = state[1][0]
    state[1][2] = state[1][1]
    state[1][3] = state[1][2]
    state[1][0] = temp1

    state[2][0],state[2][1] = state[2][2],state[2][3]

    temp2 = state[3][0] # lcl this one
    state[3][0] = state[3][1]
    state[3][1] = state[3][2]
    state[3][2] = state[3][3]
    state[3][3] = temp2

    return state

def inv_sub_bytes(state):
    Sub_box = {
        '52': '00', '09': '01', '6a': '02', 'd5': '03', '30': '04', '36': '05', 'a5': '06', '38': '07',
        'bf': '08', '40': '09', 'a3': '0a', '9e': '0b', '81': '0c', 'f3': '0d', 'd7': '0e', 'fb': '0f',
        '7c': '10', 'e3': '11', '39': '12', '82': '13', '9b': '14', '2f': '15', 'ff': '16', '87': '17',
        '34': '18', '8e': '19', '43': '1a', '44': '1b', 'c4': '1c', 'de': '1d', 'e9': '1e', 'cb': '1f',
        '54': '20', '7b': '21', '94': '22', '32': '23', 'a6': '24', 'c2': '25', '23': '26', '3d': '27',
        'ee': '28', '4c': '29', '95': '2a', '0b': '2b', '42': '2c', 'fa': '2d', 'c3': '2e', '4e': '2f',
        '08': '30', '2e': '31', 'a1': '32', '66': '33', '28': '34', 'd9': '35', '24': '36', 'b2': '37',
        '76': '38', '5b': '39', 'a2': '3a', '49': '3b', '6d': '3c', '8b': '3d', 'd1': '3e', '25': '3f',
        '72': '40', 'f8': '41', 'f6': '42', '64': '43', '86': '44', '68': '45', '98': '46', '16': '47',
        'd4': '48', 'a4': '49', '5c': '4a', 'cc': '4b', '5d': '4c', '65': '4d', 'b6': '4e', '92': '4f',
        '6c': '50', '70': '51', '48': '52', '50': '53', 'fd': '54', 'ed': '55', 'b9': '56', 'da': '57',
        '5e': '58', '15': '59', '46': '5a', '57': '5b', 'a7': '5c', '8d': '5d', '9d': '5e', '84': '5f',
        '90': '60', 'd8': '61', 'ab': '62', '00': '63', '8c': '64', 'bc': '65', 'd3': '66', '0a': '67',
        'f7': '68', 'e4': '69', '58': '6a', '05': '6b', 'b8': '6c', 'b3': '6d', '45': '6e', '06': '6f',
        'd0': '70', '2c': '71', '1e': '72', '8f': '73', 'ca': '74', '3f': '75', '0f': '76', '02': '77',
        'c1': '78', 'af': '79', 'bd': '7a', '03': '7b', '01': '7c', '13': '7d', '8a': '7e', '6b': '7f',
        '3a': '80', '91': '81', '11': '82', '41': '83', '4f': '84', '67': '85', 'dc': '86', 'ea': '87',
        '97': '88', 'f2': '89', 'cf': '8a', 'ce': '8b', 'f0': '8c', 'b4': '8d', 'e6': '8e', '73': '8f',
        '96': '90', 'ac': '91', '74': '92', '22': '93', 'e7': '94', 'ad': '95', '35': '96', '85': '97',
        'e2': '98', 'f9': '99', '37': '9a', 'e8': '9b', '1c': '9c', '75': '9d', 'df': '9e', '6e': '9f',
        '47': 'a0', 'f1': 'a1', '1a': 'a2', '71': 'a3', '1d': 'a4', '29': 'a5', 'c5': 'a6', '89': 'a7',
        '6f': 'a8', 'b7': 'a9', '62': 'aa', '0e': 'ab', 'aa': 'ac', '18': 'ad', 'be': 'ae', '1b': 'af',
        'fc': 'b0', '56': 'b1', '3e': 'b2', '4b': 'b3', 'c6': 'b4', 'd2': 'b5', '79': 'b6', '20': 'b7',
        '9a': 'b8', 'db': 'b9', 'c0': 'ba', 'fe': 'bb', '78': 'bc', 'cd': 'bd', '5a': 'be', 'f4': 'bf',
        '1f': 'c0', 'dd': 'c1', 'a8': 'c2', '33': 'c3', '88': 'c4', '07': 'c5', 'c7': 'c6', '31': 'c7',
        'b1': 'c8', '12': 'c9', '10': 'ca', '59': 'cb', '27': 'cc', '80': 'cd', 'ec': 'ce', '5f': 'cf',
        '60': 'd0', '51': 'd1', '7f': 'd2', 'a9': 'd3', '19': 'd4', 'b5': 'd5', '4a': 'd6', '0d': 'd7',
        '2d': 'd8', 'e5': 'd9', '7a': 'da', '9f': 'db', '93': 'dc', 'c9': 'dd', '9c': 'de', 'ef': 'df',
        'a0': 'e0', 'e0': 'e1', '3b': 'e2', '4d': 'e3', 'ae': 'e4', '2a': 'e5', 'f5': 'e6', 'b0': 'e7',
        'c8': 'e8', 'eb': 'e9', 'bb': 'ea', '3c': 'eb', '83': 'ec', '53': 'ed', '99': 'ee', '61': 'ef',
        '17': 'f0', '2b': 'f1', '04': 'f2', '7e': 'f3', 'ba': 'f4', '77': 'f5', 'd6': 'f6', '26': 'f7',
        'e1': 'f8', '69': 'f9', '14': 'fa', '63': 'fb', '55': 'fc', '21': 'fd', '0c': 'fe', '7d': 'ff'
    }
    # gpt generated so does not seem right ???
    # error in the decryption part debugged all steps cant figure it out 
    out = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(Sub_box[state[i][j]])
        out.append(temp)
    return out

def inv_mix_columns(state):
    fixed_inv_mix_col = [
        ['0e', '0b', '0d', '09'],
        ['09', '0e', '0b', '0d'],
        ['0d', '09', '0e', '0b'],
        ['0b', '0d', '09', '0e']
    ]
    out_mix_col = [
        ['00', '00', '00', '00'],
        ['00', '00', '00', '00'],
        ['00', '00', '00', '00'],
        ['00', '00', '00', '00']
    ]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                temperer = ''
                dot_mux_val_op = dot_mux(fixed_inv_mix_col[i][k], state[k][j])
                bin_out_mix_col = hex2bin(out_mix_col[i][j])
                for m in range(8):  # bit wise xor so
                    temperer += xor(bin_out_mix_col[m], dot_mux_val_op[m])
                out_mix_col[i][j] = bin2hex(temperer)
    return out_mix_col

def decrypt_AES(CT: str, KE: str) -> str:
    ct = CT.lower()
    ke = KE.lower()
    pt = ''

    cipher_text_matrix = convert_32hex_to_byte_array(ct)
    rounds = {32: 10, 48: 12, 64: 14}
    num_rounds = rounds[len(ke)]
    keys_for = generate_keys(ke, num_rounds)[::-1]  # Reverse the key schedule for decryption

    mat_round_key = convert_32hex_to_byte_array(''.join(keys_for[:4]))
    after_ri = mat_xor(cipher_text_matrix, mat_round_key)
    # after_ri = inv_mix_columns(after_ri)  # Only in main rounds
    after_ri = inv_shift_rows(after_ri)
    after_ri = inv_sub_bytes(after_ri)
    print('After reverse round 10 : ',after_ri)
    print('HEX format : ',convert_byte_array_to_hex(after_ri))
    for rounds_here in range(1, num_rounds):
        mat_round_key = convert_32hex_to_byte_array(''.join(keys_for[rounds_here * 4:(rounds_here + 1) * 4]))
        after_ri = inv_shift_rows(after_ri)
        after_ri = inv_sub_bytes(after_ri)
        after_ri = mat_xor(after_ri, mat_round_key)
        after_ri = inv_mix_columns(after_ri)  # Only in main rounds
        print(f'HEX format after reverse Round {num_rounds-rounds_here} : ',convert_byte_array_to_hex(after_ri))

    mat_round_key = convert_32hex_to_byte_array(''.join(keys_for[num_rounds * 4:]))  # Fix key indexing
    after_ri = mat_xor(after_ri, mat_round_key)
    print('HEX format after IP inverse using the first 2 keys : ',convert_byte_array_to_hex(after_ri))
    for row in after_ri:
        for val in row:
            pt += val

    return pt

st = '1'*128
ke = '0'*32
print(encrypt_AES(st,ke))