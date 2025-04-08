import math
import random
import sys

def modInverse(A, M):
    # use extended euvlids algo 
    ri = [max(A,M),min(A,M)]
    qi = [-1,-1]
    x = [1,0]
    y = [0,1]
    print('\n\nExtended Euclids algo starts : ')
    print(ri[-2],qi[-2],x[-2],y[-2])
    while(ri[-1] != 1):
        print(ri[-1],qi[-1],x[-1],y[-1])
        if(ri[-1] == 0):
            print('???')
            return 0
        v1 = ri[-1]
        v2 = ri[-2]
        ri.append(v2%v1)
        qi.append(v2//v1)
        x.append(x[-2] - x[-1]*qi[-1])
        y.append(y[-2] - y[-1]*qi[-1])
    
    print('Extended Euclids algo ends\n\n')
    if(A > M):
        out = x[-1]
        if(out < 0):
            out = M - out
        return out # x val used
    else:
        out = y[-1]
        if(out < 0):
            out = M - out
        return out # y val used
    
# print(modInverse(17,6))

def power(x, y, M):
    if (y == 0):
        return 1
    p = power(x, y // 2, M) % M # binary or the sqaure-sum method used
    p = (p * p) % M
    if(y % 2 == 0):
        return p
    else:
        return ((x * p) % M)# bit wise yeh 
    
def notprime(A):
    a = int(A)
    if(a == 0 or a==1):
        return True
    for i in range(2,math.ceil(math.sqrt(a+1))+2):
        if(a%int(i)==0):
            return True
    return False


maxo = int(input('Enter max bits you require : '))
if(maxo == 1 or maxo == 0):
    print('Error cant proceed cause no pair of primes can be found in ranges [1,1] or [1,2] !! ')
    sys.exit()
p =  random.randint(2,pow(2,maxo))

while(notprime(p)):
    p = random.randint(2,pow(2,maxo))
    if(p%2 == 0 or p == 1):
        p = random.randint(2,pow(2,maxo))

q = random.randint(2,pow(2,maxo))

while(notprime(q)):
    q = random.randint(2,pow(2,maxo))
    if(q == 1 or q == p or q%2 == 0):
        # chance both are same then algo doesnt work
        # obv cant be 1 cause 1 is neither prime nor co prime 
        q = random.randint(2,pow(2,maxo))
    # should be a prime all primes are odd so any last bit active ? check maybe 

# if prime not check ?

# p = 17
# q = 11
M = int(input('Message [as int] = '))
print(f'p = {p}')
print(f'q = {q}')
N = p*q
phi_n = (p-1)*(q-1) # (p-1)*(q-1)
e = random.randint(1,phi_n)
while (notprime(e)):
    e = random.randint(1,phi_n)
    # as e should be prime and less than phi_n can also be 1 so yeh
    if(e % p == 0 or e % q == 0):
        e = random.randint(1,phi_n)
print(f'e = {e}')
print(f'N = {N}')
print(f'Phi(N) = {phi_n}')
ct = power(M,e,N) # M^e mod N
print(f'Cipher int = {ct}')
d = modInverse(e,phi_n)
print(f'd = {d}') # d = e^-1 mod phi(N)
pt = power(ct,d,N) #  pt = ct^d mod N
print(f'Deciphered int = {pt}')