#!/usr/bin/python3


from pwn import *

conn = remote('localhost',1337)
print(conn.recv())
conn.sendline(b'-3')
print(conn.recvline())
print(conn.recvline())
conn.close()

