# AES128_py
AES-128 Implementation in Python 3.9

It's slow, and I'm still learning python, looking for your feedback.

With ECB & CTR Modes

-----------------------------------------------------------------------------

Command Line Arguments:

Mode:
"-ecb" --> ECB Mode   ||    "-ctr" --> CTR Mode

Operation:
"-e" --> Encrypt    ||    "-d" --> Decrypt

"-o" --> output file name   ||    output file name = input file name + (".aes" if encrypted || ".decrypted" if decrypted)

"-k" --> read key value from the following file, will be read as bytesarray   ||    key will be generated randomly

In case of CTR Mode :
"-iv" --> read IV from the following key    ||    IV will be generated randomly


-----------------------------------------------------------------------------

Example:

python3 AES.py plain.txt -ecb -k key.txt -o output encrypted
python3 AES.py cihper.aes -ctr -iv IV.txt
