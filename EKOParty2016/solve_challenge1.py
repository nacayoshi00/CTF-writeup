
encrypt_massage=list("x2dtJEOmyjacxDemx2eczT5cVS9fVUGvWTuZWjuexjRqy24rV29q")

group_by = 4
encrypt_massage_chunks = zip(*[iter(encrypt_massage)]*group_by)

encrypt_table="ZYXABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/"

for i in encrypt_massage_chunks:
    buf = 0;
    count = 0
    for j in i:
#        print j
        buf += encrypt_table.find(j) << ((3-count)*6)
        count += 1
#    for k in xrange(3):
#        print hex(buf >> 8*k)
    print hex(buf)
