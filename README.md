# AES128_py
AES-128 Implementation in Python 3.9

Multi-threaded using threading module, and threads use queues from Queue or queue module to communicate

It's slow, and I'm still learning python, looking for your feedback.

With ECB & CTR Modes

-----------------------------------------------------------------------------

Threads :

read_thread [Producer -> q1] --> Read data as states(16-Byte), check if it needs padding and do it. Then put it on q1 queue to be consumed.

operate_thread [Consumer -> q1 then Producer -> q2] --> Get data from q1 as states(16-Bytes), check the data [self.name] which was given when the thread created, do the appropriate operation. Then put the final value of the state to q1 Queue to be consumed.

write_thread [Consumer -> q2] --> Get data from q2 as states(16-Bytes), write it to the output file.

-----------------------------------------------------------------------------

Command Line Arguments:

Mode:

"-ecb" --> ECB Mode   ||    "-ctr" --> CTR Mode


Operation:

"-e" --> Encrypt    ||    "-d" --> Decrypt

"-o" --> output file name   ||    output file name = input file name + ".output"

"-k" --> read key value from the following file, will be read as bytesarray   ||    key will be generated randomly


In case of CTR Mode :

"-iv" --> read IV from the following key    ||    IV will be generated randomly


-----------------------------------------------------------------------------

Example:

[ECB-Mode Encrypted | Read Key from "key.txt" | Name the output file "output.encrypted"]

python3 AES.py plain.txt -ecb -k key.txt -o output.encrypted -enc


[CTR-Mode | Generate Random Key | Read IV frim "IV.txt" | Name output file by default "cipher.aes.output"]

python3 AES.py cihper.aes -ctr -iv IV.txt
