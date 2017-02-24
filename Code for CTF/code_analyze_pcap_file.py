
# 0. import library
import dpkt, socket
import string
import binascii
import sys

# 1. open the pcap file
fw = open("aaa.txt","w")

with open("/home/prayer/Desktop/RU3_CTF/somepang.pcap", "rb") as f:


# Read pcap file by dpkt
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
'''

# -*- coding: utf-8 -*-

import dpkt, socket
import string
import binascii
import sys

#メイン関数
def main(filename):
    pcr = dpkt.pcap.Reader(open(filename,'rb'))
    #パケット数
    packet_count = 0

    #パケット処理
    for ts,buf in pcr:
        packet_count += 1
        try:
            eth = dpkt.ethernet.Ethernet(buf)
        except:
            continue

        #IPデータの場合
        if type(eth.data) == dpkt.ip.IP:
            ip = eth.data
            ipheader(ip)
            #TCPデータ
            if type(ip.data) == dpkt.tcp.TCP:
                tcp = ip.data
                #ペイロードが0以外
                if len(tcp.data) != 0:
                    thex = binascii.b2a_hex(tcp.data)
                    payload(thex)
            #UDPデータ
            elif type(ip.data) == dpkt.udp.UDP:
                udp = ip.data
                #ペイロードが0以外
                if len(udp.data) != 0:
                    uhex = binascii.b2a_hex(udp.data)
                    payload(uhex)
            #ICMPデータ
            elif type(ip.data) == dpkt.icmp.ICMP:
                icmp = ip.data
                #ペイロードが0以外
                if len(icmp.data) != 0:
                    ihex = binascii.hexlify(str(icmp.data))
                    payload(ihex[8:])

    print "処理終了:", packet_count

#IPヘッダ処理
def ipheader(header):
    #ヘッダの処理
    src = socket.inet_ntoa(header.src)
    dst = socket.inet_ntoa(header.dst)
    #TCP
    if type(header.data) == dpkt.tcp.TCP:
        print "TCP %s:%s => %s:%s (len:%s)" % (src, header.data.sport, dst, header.data.dport, len(header.data.data))
    #UDP
    elif type(header.data) == dpkt.udp.UDP:
        print "UDP %s:%s => %s:%s (len:%s)" % (src, header.data.sport, dst, header.data.dport, len(header.data.data))
    #ICMP
    elif type(header.data) == dpkt.icmp.ICMP:
        print "ICMP %s:type %s,code %s => %s (len:%s)" % (src, header.data.type, header.data.code, dst, len(header.data.data))
    #その他
    else:
        print "%s => %s" % (src, dst)


#ペイロード
def payload(thex):
    #ペイロードの処理
    return

#メイン関数
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print "ファイルを指定して下さい"
        exit()
    #第2引数をファイル名にする
    filename = sys.argv[1]

    main(filename)















for t,buf in p
    eth = dpkt.ethernet.Ethernet(buf)

	ip = eth.data
	src = ip.src
	dst = ip.dst
	src_a = socket.inet_ntoa(src)
	dst_a = socket.inet_ntoa(dst)
	print "Sorce IP :%s"%src_a
	print "Dest IP :%s"%dst_a





import pyshark
cap = pyshark.FileCapture('/home/prayer/Desktop/RU3_CTF/somepang.pcap')
count =40004

f = open("aaa.txt","a")

result = ""


for i in xrange():

#    print cap[count].icmp.data
#    result += (cap[count].icmp.data[0:4]).decode('hex')
    f.write((cap[count].icmp.data[0:4]).decode('hex'))
    count += 2
    print str(count) +":"+(cap[count].icmp.data[0:4]).decode('hex')

#    f.write((cap[count].icmp.data[0:4]).decode('hex'))

f.close()
cap.close()
'''
