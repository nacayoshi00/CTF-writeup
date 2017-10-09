
# 0. import library
import dpkt, socket
import string
import binascii
import sys

# 1. open the pcap file
fw = open("en100par.bin","w")

with open("download_2.pcap", "rb") as f:

    time = []

# Read pcap file by dpkt
    pcr = dpkt.pcap.Reader(f)
    for t, buf in pcr:
        eth = dpkt.ethernet.Ethernet(buf)
        udp = eth.data.data
        ihex = binascii.hexlify(str(udp.data))

        # extract specific 232 bytes packet. compare the 
        if (ihex[0:10] == "2711000300") & (ihex[12:16] == "43ec") & (ihex[28:44] == "ff00000000070000"):
            print "0x"+ihex[44:48]
            
            # there is some dup packet, so I store data and timestamp to sort.
            timestamp = [int("0x"+ihex[44:48],16),ihex[48:-4]]
            time.append(timestamp)

    before_time = -1

    # sort by timestamp to correct order and remove dup packets. 
    for i in sorted(time):
        if i[0] > before_time:
            fw.write(i[1].decode('hex'))
        
        before_time = i[0]


