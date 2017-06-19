from pwn import *
from sympy import *

context(arch = 'i386', os = 'linux')
primelist=[]
count=0

while 1:

    r = remote('nttvuln2014.picoctf.com', 51818)
    # EXPLOIT CODE GOES HERE

    a = r.recvline()
    pubkey1 = int(r.recvline(),16)

    r.close()

    r = remote('nttvuln2014.picoctf.com', 51818)
    # EXPLOIT CODE GOES HERE

    a = r.recvline()
    pubkey2 = int(r.recvline(),16)

    r.close()

    prime = gcd(pubkey1,pubkey2)
    print prime
    if (prime != 1):
#        if (str(prime) in primelist == False):
            primelist.append(str(prime))
            print "+"+str(prime)
            count += 1
            if count== 60:
                break
primelist.sort()
for i in primelist:
    print i


# factorization
sympy.factorint(2016)