'''
*   Author: Adnan Omar Khalaf Hleihel
*   Created at: 19/12/2020
*   Tile: AES implementation in python (Key Scheduling header)
'''

from random import seed, getrandbits
from AES_encrypt import subbytes

rcon = ((0x01, 0x00, 0x00, 0x00),	(0x02, 0x00, 0x00, 0x00),
        (0x04, 0x00, 0x00, 0x00),	(0x08, 0x00, 0x00, 0x00),
        (0x10, 0x00, 0x00, 0x00),	(0x20, 0x00, 0x00, 0x00),
        (0x40, 0x00, 0x00, 0x00),	(0x80, 0x00, 0x00, 0x00),
        (0x1B, 0x00, 0x00, 0x00),	(0x36, 0x00, 0x00, 0x00));


key = bytearray(16)
round_key = []

def get_key(fn) :
    global key
    fp = open(fn, "rb")
    key = bytearray(fp.read(16))
    fp.close()


def gen_one_round_key(last, rnd) :
    new = bytearray(16)

    tmp = bytearray([last[13], last[14], last[15], last[12]])
    subbytes(tmp, 4)

    new[0] = last[0] ^ tmp[0] ^ rcon[rnd][0]
    tmp[0] = new[0]

    new[1] = last[1] ^ tmp[1] ^ rcon[rnd][1]
    tmp[1] = new[1]

    new[2] = last[2] ^ tmp[2] ^ rcon[rnd][2]
    tmp[2] = new[2]

    new[3] = last[3] ^ tmp[3] ^ rcon[rnd][3]
    tmp[3] = new[3]

    for i in range(4, 16, 4) :
        new[i] = last[i]   ^ tmp[0]
        tmp[0] = new[i]

        new[i+1] = last[i+1] ^ tmp[1]
        tmp[1] = new[i+1]

        new[i+2] = last[i+2] ^ tmp[2]
        tmp[2] = new[i+2]

        new[i+3] = last[i+3] ^ tmp[3]
        tmp[3] = new[i+3]

    return new


def gen_round_keys() :
    global key
    global round_key
    round_key.append(gen_one_round_key(key, 0))

    for i in range(9) :
        round_key.append(gen_one_round_key(round_key[i], i+1))


def gen_random_key() :
    global key
    seed()
    for i in range(16) :
        key[i] = getrandbits(8)
