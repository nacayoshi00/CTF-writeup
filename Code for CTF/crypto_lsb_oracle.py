'''
#!/usr/bin/env python2
from pwn import *
from Crypto.Util.number import long_to_bytes,bytes_to_long

n = 120357855677795403326899325832599223460081551820351966764960386843755808156627131345464795713923271678835256422889567749230248389850643801263972231981347496433824450373318688699355320061986161918732508402417281836789242987168090513784426195519707785324458125521673657185406738054328228404365636320530340758959
e = 65537

C = 2201077887205099886799419505257984908140690335465327695978150425602737431754769971309809434546937184700758848191008699273369652758836177602723960420562062515168299835193154932988833308912059796574355781073624762083196012981428684386588839182461902362533633141657081892129830969230482783192049720588548332813

oracle_process = process(["wine", "./lsb_oracle.vmp.exe", "/decrypt"])
def oracle(CIN):
    oracle_process.recvuntil("done.\r\n")
    oracle_process.sendline(str(CIN))
    return int(oracle_process.readline().strip())


UP = n
LOW = 0

cur_C = C
for i in range(n.bit_length()):
    cur_C = (cur_C * (2**e % n)) %n
    if oracle(cur_C) == 0:
        UP = (UP + LOW)/2
    else:
        LOW = (UP + LOW)/2
    print UP-LOW

pt =  long_to_bytes(UP)

print hex(UP)

for x in range(256):
    for y in range(256):
        corr_pt = pt[:-2] + chr(x) + chr(y)
        if pow(bytes_to_long(corr_pt), e, n) == C:
            print corr_pt
            exit()



'''

from pwn import *
from fractions import Fraction
import time
from Crypto.Util.number import long_to_bytes,bytes_to_long

n = 120357855677795403326899325832599223460081551820351966764960386843755808156627131345464795713923271678835256422889567749230248389850643801263972231981347496433824450373318688699355320061986161918732508402417281836789242987168090513784426195519707785324458125521673657185406738054328228404365636320530340758959
e = 65537
ctext = 2201077887205099886799419505257984908140690335465327695978150425602737431754769971309809434546937184700758848191008699273369652758836177602723960420562062515168299835193154932988833308912059796574355781073624762083196012981428684386588839182461902362533633141657081892129830969230482783192049720588548332813



p = process(['./lsb_oracle.vmp.exe', '/decrypt'])

bounds = [0, n]
diff = bounds[1]-bounds[0]
count = 0

while 1:
    r = p.recvline()
    print r
    ctext = (ctext * pow(2, e, n)) % n
    p.send(str(ctext)+"\n")
    r = p.recvline()


    if r[0:1] == "0":
        log.info("[+] LSB = 0")
        bounds[1] = (bounds[1]+bounds[0])/2

    elif r[0:1] == "1":
        log.info("[+] LSB = 1")
        bounds[0] = (bounds[1]+bounds[0])/2

    diff = bounds[1]-bounds[0]
    log.info("[+] diff = "+str(diff))
    log.info("[+] count = "+str(count))
    if diff == 0:
        if count == 1:
            m = bounds[1]
            log.info("[+] Plain text = "+long_to_bytes(m))
            break
        count += 1
