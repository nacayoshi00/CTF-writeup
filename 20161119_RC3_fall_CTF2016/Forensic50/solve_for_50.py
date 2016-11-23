import dpkt, socket
import string
import binascii
import sys

count = 0
fw = open("aaa.txt","w")

with open("/home/prayer/Desktop/RU3_CTF/somepang.pcap", "rb") as f:
    pcr = dpkt.pcap.Reader(f)
    for t, buf in pcr:
        eth = dpkt.ethernet.Ethernet(buf)
        icmp = eth.data.data
        ihex = binascii.hexlify(str(icmp.data))


        if count % 2 == 0:
            print ihex[24:28].decode('hex')
            fw.write(ihex[24:28].decode('hex'))


        count += 1

fw.close()
f.close()
