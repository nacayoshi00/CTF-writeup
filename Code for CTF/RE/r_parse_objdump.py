
f = open("ba09.txt","r")

buf = 0
flag = "____________________"
flag_list = list(flag)
count = 0

for i in f:
    if i[0:3] == "mov":
        if i.split("[")[1].split("]")[0] != "r9":
            count = int(i.split("+")[1].split("]")[0],16)
        else:
            count = 0
    elif i[0:3] == "xor":
        buf = int(i.split("    ")[1].split(",")[1],16)
        #print buf
    elif i[0:3] == "cmp":
        buf ^= int(i.split("    ")[1].split(",")[1],16)
        print count
        flag_list[count] = chr(buf)
flag = "".join(flag_list)
print flag