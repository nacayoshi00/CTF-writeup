'''
At first, We tried to make first 24 bytes of PNG file.
We can find first 16 bytes because it's fixed "89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52"
Also I could find rest 8bytes by the filename because This picture is 1920x1080(fullhd) file.

So I could restore the key.

'''



plain = [0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A,0x00,0x00,0x00,0x0D,0x49,0x48,0x44,0x52,0x00,0x00,0x07,0x80,0x00,0x00,0x04,0x38]

plain ="89504E470D0A1A0A0000000D494844520000078000000438".decode("hex")

enc = "FB3B26625C5A2E6D3026336A7D7E04662A2561A8554E2764".decode("hex")


def supa_encryption(s1, s2):
    res = [chr(0)]*24
    for i in range(len(res)):
        q = ord(s1[i])
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
    res = ''.join(res)
    return res

def add_pad(msg):
    L = 24 - len(msg)%24
    msg += chr(L)*L
    return msg



key = supa_encryption(plain, enc)

with open('BITSCTFfullhd.png','rb') as f:
    data = f.read()

data = add_pad(data)

dec_data = ''
for i in range(0, len(data), 24):
    dec = supa_encryption(data[i:i+24], key)
    dec_data += dec

with open('fullhd.png', 'wb') as f:
    f.write(dec_data)


'''
def add_pad(msg):
    L = 24 - len(msg)%24
    msg += chr(L)*L
    return msg

with open('fullhd.png','rb') as f:
    data = f.read()

data = add_pad(data)


with open('key.txt') as f:
    key = f.read()

enc_data = ''
for i in range(0, len(data), 24):
    enc = supa_encryption(data[i:i+24], key)
    enc_data += enc

with open('BITSCTFfullhd.png', 'wb') as f:
    f.write(enc_data)
'''
