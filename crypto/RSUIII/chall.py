#!/bin/python

from Crypto.Util.number import getPrime
from binascii import hexlify
from ptrlib import chunks
from FLAG import flag

n = getPrime(256)*getPrime(256)

def rsa_enc(pt: bytes):
    e = 5
    pt = int(hexlify(pt), 16) 
    return pow(pt,e,n)

pt = chunks(flag, 8)

ct = [None] * len(pt)

for i in range(len(pt)):
    ct[i] = rsa_enc(pt[i])

print(f'ct = {ct}')

