

f = open("final.txt","r")

text = f.read()

flag = ""

for i in text:
    if i.isupper():
        flag += i

flag_bin = flag.replace("ZERO","0").replace("ONE","1")

flag_s = ""

for i in xrange(0,len(flag_bin),8):
    flag_s += chr(int(flag_bin[i:i+8],2))

print flag_s
