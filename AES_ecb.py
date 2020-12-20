'''
*   Author: Adnan Omar Khalaf Hleihel
*   Created at: 19/12/2020
*   Tile: AES implementation in python (ECB Mode)
'''

import AES_encrypt as aes_enc
import AES_decrypt as aes_dec
import AES_key_sched as aes_key


def print_bytes(arg) :
    for i in range(16) :
        print(hex(arg[i]), end = "\t")
    print("\n")


def encrypt(fn, fnw, size, extra, kfn) :
    if fnw == 0 :   fnw = fn + ".aes"
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
        if i == (size-1) :
            for i in range(extra, 16) :
                state.append(0x00)

        aes_enc.encrypt_one_state(state, aes_key.key, aes_key.round_key)

        print("%010d" % i, end = "")
        print("\b"*10, end = "")

        fpw.write(state)

    print("\n")
    fp.close()
    fpw.close()


def decrypt(fn, fnw, size, extra, kfn) :
    if fnw == 0 :   fnw = fn+".decrypted"
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

        aes_dec.decrypt_one_state(state, aes_key.key, aes_key.round_key)

        print("%010d" % i, end = "")
        print("\b"*10, end = "")

        if i == (size-1) :
            while not state[len(state)-1] :
                state.pop()
        fpw.write(state)

    print("\n")
    fp.close()
    fpw.close()
