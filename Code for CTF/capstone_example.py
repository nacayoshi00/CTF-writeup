'''
To determine arch and mode
http://www.capstone-engine.org/lang_python.html
'''


from capstone import *
import re

#CODE = b"\x55\x48\x8b\x05\xb8\x13\x00\x00"

f = open("./SCrack.elf","r")
#f.seek(0x6f2)
#data = f.read(0x600)
data = f.read()
#print data.encode("hex")

flag = ""

offset = 0x0000000000400960
ptr = 0x0000000000400C4A - offset

md = Cs(CS_ARCH_X86, CS_MODE_64)
for i in md.disasm(data[ptr:ptr+0x320], ptr+offset):
    if i.mnemonic == "mov":
        if (len(i.op_str.split(', ')[1]) == 4) & (i.op_str.split(', ')[0] == "esi"):
            char = i.op_str.split(', ')[1]
            flag += chr(int(char,16))
            print("%s" %(i.op_str))

print flag
