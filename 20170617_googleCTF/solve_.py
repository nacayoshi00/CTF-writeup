'''
file = [0x49 ,0x5E ,0x52 ,0x5A ,0x79 ,0x1B ,0x7B ,0x5A ,0x7C ,0x5B ,0x66 ,0x5A ,0x5A ,0x5A ,0x48 ,0x5A ,0x6F ,0x1A ,0x55 ,0x5A ,0x12 ,0x58 ,0x5B ,0x5A ,0x0E ,0x09 ,0x5F ,0x5A ,0x12 ,0x59 ,0x59 ,0x5A ,0xED ,0x68 ,0xD7 ,0x78 ,0x15 ,0x58 ,0x5B ,0x5A ,0x82 ,0x5A ,0x5A ,0x5B ,0x72 ,0xA8 ,0x78 ,0x5A ,0x45 ,0x5A ,0x2A ,0x7A ,0x7E ,0x5A ,0x4A ,0x5A ,0x40 ,0x5B ,0x5A ,0x5A ,0x34 ,0x7A ,0x7F ,0x5A ,0x4A ,0x5A ,0x50 ,0x5A ,0x63 ,0x5A ,0x47 ,0x5A ,0x0E ,0x0A ,0x58 ,0x5A ,0x34 ,0x4A ,0x5B ,0x5A ,0x5A ,0x5A ,0x56 ,0x5A ,0x78 ,0x5B ,0x45 ,0x5A ,0x38 ,0x58 ,0x5E ,0x5A ,0x0E ,0x09 ,0x5F ,0x5A ,0x2B ,0x7A ,0x78 ,0x5A ,0x68 ,0x5A ,0x56 ,0x58 ,0x2A ,0x7A ,0x7E ,0x5A ,0x7B ,0x5A ,0x48 ,0x48 ,0x2B ,0x6A ,0x4F ,0x5A ,0x4A ,0x58 ,0x56 ,0x5A ,0x34 ,0x4A ,0x4C ,0x5A ,0x5A ,0x5A ,0x54 ,0x5A ,0x5A ,0x59 ,0x5B ,0x5A ,0x52 ,0x5A ,0x5A ,0x5A ,0x40 ,0x41 ,0x44 ,0x5E ,0x4F ,0x58 ,0x48 ,0x5D ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00]

xor= 0x5a
res = ""

for i in file:
    res += chr(i^xor) 
print res

'''
#str = [0x1D650B6E, 0x1377416F, 0x16724D62, 0x5320096C, 0x5691D74, 0x86E5A75, 0x4420046B, 0x6F096F, 0x4D634620, 0x10640D6E, 0x4F614520, 0x0A660265, 0x0A650D62, 0x47204A64, 0x36E1A75, 0x0C6F5D72, 0x6675420, 0x4650C68, 0x5B744120, 0x10640564, 0x25410F20]
# /data/data/com.google.ctf.food/files/d.dex

#str = [0x69695820, 0x17720D69, 0x1B745C73, 0x53200164, 0x26E0861, 0x4620032C, 0x17730A65, 0x0D621375, 0x4D634620, 0x1A6E0C6F, 0x426C096C, 0x5691275, 0x6F0D62, 0x47205C72, 0x8651976, 0x0C6F0F20, 0x465186C, 0x362096D, 0x5A751372, 0x37434120, 0x4A2E4B64]
# /data/data/com.google.ctf.food/files/odex

#str = [0x72721169, 0x11743753, 0x0E204A2E, 0x5C731D65, 0x11741175, 0x16E4669, 0x1E6D4520, 0x1B770C65, 0x660F20, 0x5614F20, 0x1D72096F, 0x48664620, 0x1F6B0C6F, 0x416F0663, 0x4C20086F, 0x1B744F20, 0x2655B75, 0x36E0669, 0x1774416E, 0x0E6F1763, 0x41205F3B, 0x4A650F6E, 0x1D691677, 0x4420416E]
# /data/data/com.google.ctf.food/files/odex/d.dex

#str = [0x20207F2C, 0x5C730165, 0x6F1B74, 0x761426D, 0x96F0074, 0x43204B64, 0x651C70, 0x1770006F, 0x7680463, 0x0F20036E, 0x6694320]
# com/google/ctf/food/S

#str = [0x6E6E0E61, 0x5320022C, 0x0E631F69, 0x86C1072, 0x8610B67]
# libdvm.so

#str = [0x0B720470, 0x8610670, 0x49201C68, 0x17742869, 0x13774F20, 0x16E296F, 0x5C730561, 0x0A653C53, 0x4620012E, 0x3650074, 0x10734E61, 0x15704C20, 0x86F1B74, 0x0E610A6D, 0x406F1974, 0x4F200764]
#com/google/ctf/food/FoodActivity

#str = [0x96B1E69]
# wb

#str = [0x2700065, 0x14704120, 0x0A65226E, 0x1D6E1665, 0x18790D61, 0x20635820, 0x492C3672, 0x4A650964, 0x12771B6F, 0x3705920, 0x1A69436C, 0x2690168, 0x15634C20, 0x4D2C0561]
#dalvik/system/DexClassLoader

#str = [0x3E680920, 0x53681567, 0x0C690C68, 0x41201D72, 0x29650576, 0x1C6F4120, 0x6C2A69, 0x406F0562, 0x4E200061, 0x4C20406F, 0x15745620, 0x667046E, 0x25694972, 0x25424E20, 0x472E0072, 0x11652370, 0x5F700265, 0x1E704120, 0x864416E, 0x615620, 0x1574066C, 0x2D614873, 0x4720006E, 0x695220, 0x6723A69, 0x5B743453, 0x4E204F2E, 0x15794A65, 0x0D6C0573, 0x13720B61, 0x3C701B20, 0x364006E, 0x8615220, 0x582C3C6F, 0x416E0661, 0x9670465, 0x1E72406F, 0x41205A2C, 0x0D6C0369, 0x3F734961]
#(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)V

#str = [0x5C625420, 0x452C1C72, 0x0C654C70]
# <init>

#str = [0x6565566D, 0x1E6D1A69, 0x12734C20, 0x2764416E, 0x6614E20, 0x4D2C1E72, 0x4A651776, 0x196F2243, 0x4A20622E, 0x5E77546F, 0x0B6C4E20, 0x46D0775, 0x1D693764, 0x4A650A6D, 0x4E200E6F, 0x18740F20, 0x15741761, 0x4650268, 0x6C204D65]
#(Ljava/lang/String;)Ljava/lang/Class;

#str = [0x73733761, 0x4A635863, 0x166F5420, 0x0E67186E, 0x690672, 0x11722869, 0x5B740373, 0x50204D2C, 0x5C730165, 0x1D741A75, 0x1C6E0D69, 0x36D4120, 0x7C301139]
# (Landroid/app/Activity;)V

#str = [0x172C0A73, 0x1A6E0861, 0x13650B62, 0x54201A79, 0x2465416E, 0x14641969, 0x0A6B0F20, 0x0A6E0069, 0x4F200072, 0x0D691A74, 0x32536C20]
#Landroid/app/Activity;

#str = [0x572E0D79, 0x56C1A6C, 0x8611A6E, 0x0C6F0869]
# activity

# str = [0x61611F6C, 50200061, 0x4D20416E, 0x0F694C20, 0x96C1A69, 0x406F4320, 0x1B741361, 0x15656748]
# /proc/self/m s

str = [0x1B631075, 0x5615D73, 0x44204A65]
# /d.dex

# str = [0x67670072]
# r

def parse_to_byte(val):
    byte = []
    byte.append((val>>24)&0xff) # BYTE3
    byte.append((val>>16)&0xff) # BYTE2
    byte.append((val>>8)&0xff)  # BYTE1
    byte.append((val)&0xff)
    return byte

flag = ""
#for i in str:

string = ""

for i in str:
    byte_array = parse_to_byte(i)

    string += chr(byte_array[0]^byte_array[1])
    string += chr(~((byte_array[2] | ~byte_array[3]) & (byte_array[3] | ~byte_array[2])))


print string[::-1]


flag = [ -19,  116,  58,  108,  -1,  33,  9,  61,  -61,  -37,  108,  -123,  3,  35,  97,  -10,  -15,  15,  -85,  -66,  -31,  -65,  17,  79,  31,  25,  -39,  95,  93,  1,  -110,  -103,  -118,  -38,  -57,  -58,  -51,  -79]

for i in flag:
    if i < 0:
        print hex(0x100+i)
    else:
        print hex(i)
