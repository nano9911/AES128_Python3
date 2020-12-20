'''
*   Author: Adnan Omar Khalaf Hleihel
*   Created at: 19/12/2020
*   Tile: AES implementation in python (CTR Mode)
'''

from random import seed, getrandbits
import AES_encrypt as aes_enc
import AES_key_sched as aes_key


def print_bytes(arg) :
    for i in range(16) :
        print(hex(arg[i]), end = "\t")
    print("\n")


def encrypt(fn, fnw, IVfn, size, extra, kfn) :
    if fnw == 0 :   fnw = fn + ".aes"
    IV = bytearray(16)
    if not IVfn :    gen_random_iv(IV)
    else : get_iv(IVfn, IV)

    print("IV :", end = "\t")
    print_bytes(IV)

    fp = open(fn, "rb")
    fpw = open(fnw, "wb")
    if kfn == 0 :   gen_random_key()
    else :  aes_key.get_key(kfn)
    print("Key :", end = "\t")
    print_bytes(aes_key.key)
    print("\n\t\t\t")
    aes_key.gen_round_keys()

    for i in range(size) :
        state = bytearray(fp.read(16))
        if i == (size-1) :
            for i in range(extra, 16) :
                state.append(0x00)

        aes_enc.encrypt_one_state(IV, aes_key.key, aes_key.round_key)
        for e in range(16) :    state[e] ^= IV[e]

        print("%010d" % i, end = "")
        print("\b"*10, end = "")

        fpw.write(state)
        for e in range(15, -1, -1) :
            if (IV[e]+1) > 0xff :
                IV[e] = 0x00
                continue
            IV[e] += 1
            break

    print("\n")
    fp.close()
    fpw.close()


def decrypt(fn, fnw, IVfn, size, extra, kfn) :
    if fnw == 0 :   fnw = fn+".decrypted"
    IV = bytearray(16)
    if not IVfn :    gen_random_iv(IV)
    else : get_iv(IVfn, IV)
    
    print("IV :", end = "\t")
    print_bytes(IV)

    fp = open(fn, "rb")
    fpw = open(fnw, "wb")
    if kfn == 0 :   gen_random_key()
    else :  aes_key.get_key(kfn)
    print("Key :", end = "\t")
    print_bytes(aes_key.key)
    print("\t\t\t")
    aes_key.gen_round_keys()

    for i in range(size) :
        state = bytearray(fp.read(16))

        aes_enc.encrypt_one_state(IV, aes_key.key, aes_key.round_key)
        for e in range(16) :    state[e] ^= IV[e]

        print("%010d" % i, end = "")
        print("\b"*10, end = "")

        if i == (size-1) :
            while not state[len(state)-1] :
                state.pop()
        fpw.write(state)

        for e in range(15, -1, -1) :
            if (IV[e]+1) > 0xff :
                IV[e] = 0x00
                continue
            IV[e] += 1
            break

    print("\n")
    fp.close()
    fpw.close()


def gen_random_iv(IV) :
    seed()
    for i in range(16) :
        IV[i] = getrandbits(8)


def get_iv(fn, IV) :
    fp = open(fn, "rb")
    IV = bytearray(fp.read(16))
    fp.close()
