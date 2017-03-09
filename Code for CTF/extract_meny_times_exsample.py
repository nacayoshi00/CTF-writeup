

import os,time
from pwn import *

while 1:

    f = process(["/usr/bin/file", "26685"])
    line = f.readline()
    f.close()
    print line
    if "POSIX tar archive (GNU)" in line:
        os.system("mv 26685 26685.tar")
        os.system("tar -xf 26685.tar")
        os.system("rm 26685.tar")

    elif "ZPAQ stream, level 1" in line:
        os.system("zpaq x 26685 26685.out")
        os.system("mv 26685.out 26685")

    elif "XZ compressed data" in line:
        os.system("mv 26685 26685.xz")
        os.system("xz -d 26685.xz")

#        f = process(["/bin/rm", "26685.xz"])
#        f.close()
    elif "bzip2 compressed data" in line:
        os.system("bzip2 -d 26685")
        os.system("mv 26685.out 26685")

    elif "LZMA compressed data" in line:
        os.system("mv 26685 26685.lzma")
        os.system("lzma --decompress 26685.lzma")
        os.system("rm 26685.lzma")

    elif "lzip compressed data" in line:
        os.system("lzip -d 26685")
        os.system("mv 26685.out 26685")

    elif "7-zip archive data" in line:
        os.system("mv 26685 26685.7z")
        os.system("7za x 26685.7z")
        os.system("rm 26685.7z")

    elif "ARJ archive data" in line:
        os.system("mv 26685 26685.arj")
        os.system("arj e 26685.arj")
        os.system("rm 26685.arj")

    elif "gzip compressed data" in line:
        os.system("mv 26685 26685.tgz")
        os.system("tar -zxf 26685.tgz")
        os.system("rm 26685.tgz")

    elif "NuFile archive " in line:
        os.system("mv 26685 26685.a")
        os.system("/opt/share/nulib2/nulib2/nulib2 -x 26685.a")
        os.system("rm 26685.a")

    elif "Zoo archive data" in line:
        os.system("mv 26685 26685.zoo")
        os.system("zoo -extract 26685.zoo")
        os.system("rm 26685.zoo")

    elif "Zip archive data" in line:
        os.system("mv 26685 26685.zip")
        os.system("unzip 26685.zip")
        os.system("rm 26685.zip")

    else:
        break

    time.sleep(0.5)
'''
    elif "" in line:
    elif "" in line:

    raw_input()


    /opt/share/nulib2/nulib2/nulib2 -x 26685

    zpaq x 26685
    zpaq x 26685

    lzip -d 26685
    mv 26685.out 26685

    mv 26685 26685.lzma
    lzma --decompress 26685.lzma

    mv 26685 26685.zoo
    zoo -extract 26685
    '''
