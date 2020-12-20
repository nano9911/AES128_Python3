'''
*   Author: Adnan Omar Khalaf Hleihel
*   Created at: 19/12/2020
*   Tile: AES implementation in python
'''

import sys
import AES_ecb as ecb
import AES_ctr as ctr
from AES_key_sched import get_key, gen_random_key, gen_round_keys, key

def get_file_size(fn) :
    fp = open(fn, "rb")
    fp.seek(0, 2)
    size = fp.tell()
    extra = 0

    print("\nFile size = ", size, " Bytes")
    if size%16 != 0 :
        extra = size % 16
        size = int(size/16) + 1
    else :   size = int(size / 16)
    print("File size = ", size, " Blocks")

    fp.close()
    return size, extra


def print_bytes(arg) :
    for i in range(16) :
        print(hex(arg[i]), end = "\t")
    print("\n")


def main(argv) :
    if argv[1] == 0 :   infn = 0
    else :  infn = argv[1]
    size, extra = get_file_size(infn)
    outfn = 0
    kfn = 0
    IVfn = 0

    if "-k" in argv :
        kfn = argv[argv.index("-k")+1]

    if "-o" in argv :
        outfn = argv[argv.index("-o")+1]


    if ("-enc" in argv) & ("-ecb" in argv) :
        ecb.encrypt(infn, outfn, size, extra, kfn)

    elif ("-dec" in argv) & ("-ecb" in argv) :
        ecb.decrypt(infn, outfn, size, extra, kfn)

    elif ("-enc" in argv) & ("-ctr" in argv) :
        ivfn = 0
        if "-iv" in argv :  IVfn = argv[argv.index("-iv")+1]
        ctr.encrypt(infn, outfn, IVfn, size, extra, kfn)

    elif ("-dec" in argv) & ("-ctr" in argv) :
        ivfn = 0
        if "-iv" in argv :  IVfn = argv[argv.index("-iv")+1]
        ctr.decrypt(infn, outfn, IVfn, size, extra, kfn)


main(sys.argv)
