from capstone import *
import re

#CODE = b"\x55\x48\x8b\x05\xb8\x13\x00\x00"

f = open("./easyarm.arm","r")
#f.seek(0x6f2)
#data = f.read(0x600)
data = f.read()
#print data.encode("hex")

flag = ""

offset = 0xdec
ptr = 0x000614


flag = "00000000000000000000000000000000000000000000000000"
flag =list(flag)

print data[ptr:offset].encode("hex")

md = Cs(CS_ARCH_ARM, CS_MODE_THUMB)
pos=0
for i in md.disasm(data[ptr:offset], offset-ptr):
    
    if (i.mnemonic =="adds") :
        print i.op_str
        pos = int(i.op_str.split("#")[1],16)
        
    if (i.mnemonic =="cmp") & (i.op_str != "r3, #0"):
        print "pos = %d: char = %c" %(pos, chr(int(i.op_str.split("#")[1],16)))
        
        flag[pos] = chr(int(i.op_str.split("#")[1],16))
        #print ("%s" %(i.op_str.split("#")[1]))
    


    print("%s %s" %(i.mnemonic,i.op_str))


print flag
'''
['0', 'l', 'a', 'g', 'F', 'A', 'R', 'M', '_', 'I', 's', '_', 'N', 'o', 't', '_', 'S', 'c', 'a', 'r', 'y', '0', '0', '0', '0', '0', '0', '0', '0', '0
', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

Flag:ARM_Is_Not_Scary
'''
