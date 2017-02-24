from pwn import *
import re, sys


def solve_matrix(matrixa, matrixb):
	out = [[0 for x in xrange(3)] for x in xrange(3)]
	for rn in xrange(3):
		for cn in xrange(3):
			out[cn][rn] = int(matrixb[rn][cn])^int(matrixa[rn][cn])
	return out

count = 0

def printmat(matrix):
	for row in matrix:
		for value in row:
			print value,
		print ""
	print ""

def genBlockMatrix(s):
	outm = [[[7 for x in xrange(3)] for x in xrange(3)] for x in xrange(len(s)/9)]
	for matnum in xrange(0,len(s)/9):
		for y in xrange(0,3):
			for x in xrange(0,3):
				outm[matnum][y][x] = s[(matnum*9)+x+(y*3)]
	return outm

def pad(s):
	if len(s)%9 == 0:
		return s
	for i in xrange((9-(len(s)%9))):
		s.append(0)
	return s


while 1:
    count += 1
    output = []
    print "[+]"+str(count)
    conn = remote('vermatrix.pwn.democrat',4201)
    line = conn.recvline()
    seed = line.split(" ")[1]
    print seed

    blocks = genBlockMatrix(pad([ord(c) for c in seed]))
    print "[+]blocks[0]"
    printmat(blocks[0])	  	#seed1
    print "[+]blocks[1]"
    printmat(blocks[1])   	#seed2

    line = conn.recvline()
    print line
    line = line.split("\n")[0]
    output.append(line.split(" "))
    line = conn.recvline()
    print line
    line = line.split("\n")[0]
    output.append(line.split(" "))
    line = conn.recvline()
    print line
    line = line.split("\n")[0]
    output.append(line.split(" "))
    print "[+]decode_blocks[1]"
    printmat(output)

    res = solve_matrix(output, blocks[1])
    print "[+]decode_blocks[1]"
    printmat(res)
    res = solve_matrix(res, blocks[0])
    print "[+]decode_blocks[0]"
    printmat(res)

    res_str = ""
    for y in xrange(0,3):
        for x in xrange(0,3):
            res_str += str(res[y][x])+","
    res_str = res_str[:-1]
    data = res_str.replace(' ', '').strip().split(',')

    print len(data)
    print res_str
#	sleep(5)
    conn.send(res_str)
    conn.interactive()
