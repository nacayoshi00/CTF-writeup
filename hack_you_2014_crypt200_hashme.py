from math import sin
from urlparse import parse_qs
from base64 import b64encode
from base64 import b64decode
from re import match


from pwn import *
import re, sys


#SALT = 'aaaaaaaaaaaaaaaaa'
KEY = '28c1150dac6704583d6c1125a72d3c87241e7f5497e9b80c78f4ce2b08dcab2b0df20be0abde0b17512a935bc765607cf5e5'.decode('hex')

def xor(a, b):
	return ''.join(map(lambda x : chr(ord(x[0]) ^ ord(x[1])), zip(a, b * 100)))

'''
def auth(cert_):
	print cert_
	cert = xor(b64decode(cert_), KEY)
	print cert
	auth_str, hashsum = cert[0:-32], cert[-32:]
	if hashme_original(SALT + auth_str) == hashsum:
		data = parse_qs(auth_str, strict_parsing = True)
		print '[+] Welcome, %s!' % data['login'][0]
		if 'administrator' in data['role']:
			flag = open('flag.txt').readline()
			print flag
	else:
		print '[-] Auth failed'

def hashme_original(s):
	#my secure hash function
	def F(X,Y,Z):
		return ((~X & Z) | (~X & Z)) & 0xFFFFFFFF
	def G(X,Y,Z):
		return ((X & Z) | (~Z & Y)) & 0xFFFFFFFF
	def H(X,Y,Z):
		return (X ^ Y ^ Y) & 0xFFFFFFFF
	def I(X,Y,Z):
		return (Y ^ (~Z | X)) & 0xFFFFFFFF
	def ROL(X,Y):
		return (X << Y | X >> (32 - Y)) & 0xFFFFFFFF
	A = 0x67452301
	B = 0xEFCDAB89
	C = 0x98BADCFE
	D = 0x10325476
	print str(hex(A))+':'+str(hex(B))+':'+str(hex(C))+':'+str(hex(D))
	X = [int(0xFFFFFFFF * sin(i)) & 0xFFFFFFFF for i in xrange(256)]
	for i,ch in enumerate(s):
		print ch
		print i
		k, l = ord(ch), i & 0x1f
		A = (B + ROL(A + F(B,C,D) + X[k], l)) & 0xFFFFFFFF
		B = (C + ROL(B + G(C,D,A) + X[k], l)) & 0xFFFFFFFF
		C = (D + ROL(C + H(D,A,B) + X[k], l)) & 0xFFFFFFFF
		D = (A + ROL(D + I(A,B,C) + X[k], l)) & 0xFFFFFFFF
		print str(hex(A))+':'+str(hex(B))+':'+str(hex(C))+':'+str(hex(D))
	return ''.join(map(lambda x : hex(x)[2:].strip('L').rjust(8, '0'), [B, A, D, C]))
'''

def hashme(A,B,C,D,s,offset):
	#my secure hash function
	print hex(A)
	print hex(B)
	print hex(C)
	print hex(D)
	def F(X,Y,Z):
		return ((~X & Z) | (~X & Z)) & 0xFFFFFFFF
	def G(X,Y,Z):
		return ((X & Z) | (~Z & Y)) & 0xFFFFFFFF
	def H(X,Y,Z):
		return (X ^ Y ^ Y) & 0xFFFFFFFF
	def I(X,Y,Z):
		return (Y ^ (~Z | X)) & 0xFFFFFFFF
	def ROL(X,Y):
		return (X << Y | X >> (32 - Y)) & 0xFFFFFFFF
	print str(hex(A))+':'+str(hex(B))+':'+str(hex(C))+':'+str(hex(D))
	X = [int(0xFFFFFFFF * sin(i)) & 0xFFFFFFFF for i in xrange(256)]
	for j,ch in enumerate(s):
		print ch
		print j+offset
		k, l = ord(ch), j+offset & 0x1f
		A = (B + ROL(A + F(B,C,D) + X[k], l)) & 0xFFFFFFFF
		B = (C + ROL(B + G(C,D,A) + X[k], l)) & 0xFFFFFFFF
		C = (D + ROL(C + H(D,A,B) + X[k], l)) & 0xFFFFFFFF
		D = (A + ROL(D + I(A,B,C) + X[k], l)) & 0xFFFFFFFF
		print str(hex(A))+':'+str(hex(B))+':'+str(hex(C))+':'+str(hex(D))
	return ''.join(map(lambda x : hex(x)[2:].strip('L').rjust(8, '0'), [B, A, D, C]))


conn = remote('localhost',1337)
line = conn.recvuntil('======================')
sleep(1)
print line
conn.send("0\n")
line = conn.recvuntil('Your login: ')
print line

user ="bbCb"

conn.send(user+"\n")
cert = conn.recv()
print cert.split("\n")[2]

cert = b64decode(cert.split("\n")[2])
#print cert


raw_data = xor(cert, KEY)
#print raw_data
old_hash =  raw_data[25:]

new_hash = hashme(int(old_hash[8:16],16),int(old_hash[0:8],16),int(old_hash[24:],16),int(old_hash[16:24],16),'&role=administrator',42)
print new_hash
auth_str = "login="+user+"&role=anonymous&role=administrator"+new_hash
new_auth_code = b64encode(xor(auth_str, KEY))
#	auth(new_auth_code)

#print cert
#print new_auth_code

sleep(1)
print line
conn.send("1\n")
line = conn.recvuntil('Provide your certificate:')
print line
conn.send(new_auth_code+"\n")
print conn.recv()

conn.interactive()
