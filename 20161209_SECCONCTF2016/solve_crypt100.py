import md5

num = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}'

data ="LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ"

key_header = "VIGENERE"
find = [0,0,0,0]

while 1:
    key = key_header + num[find[0]] + num[find[1]] + num[find[2]] + num[find[3]]
    key_len = len(key)
    print key
    result = ''
    key_count = 0
    for i in data:
    #    print  num.index(i)
    #    print  (len(num)+ num.index(i) - num.index(key[key_count % key_len])) % len(num)
        result += num[(len(num) + num.index(i) - num.index(key[key_count % key_len])) % len(num)]
        key_count += 1
    print result

    md5_hash = md5.new(result).digest()
    print md5_hash.encode('hex')
    if   md5_hash.encode('hex') == "f528a6ab914c1ecf856a1d93103948fe":
        break

    find[0] += 1
    if find[0] > len(num)-1:
        find[0] = 0
        find[1] += 1
        if find[1] > len(num)-1:
            find[1] = 0
            find[2] += 1
            if find[2] > len(num)-1:
                find[2] = 0
                find[3] += 1
