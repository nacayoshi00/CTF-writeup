- pcap file 
    how to extract file from pcap
    https://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only

    tshark -r infile -T fields -e data | tr -d '\n' > tempfile
     -if you need to extract more than 2 field, you can use "-e xxxx -e yyyy ..."

     $ tshark -r shattered.pcapng  -T fields -e data.data -e tcp.segment_data  | tr -d ':'| tr -d '\t'> aa.txt

     convert ascii hex -> bin
        import binascii
        import sys
        string = open(sys.argv[1],'r').read()
        sys.stdout.write(binascii.unhexlify(string)) # needs to be stdout.write to avoid trailing newline
    
    other usefle tool
    - tcpflow 
    - python dpkt, scapy,
