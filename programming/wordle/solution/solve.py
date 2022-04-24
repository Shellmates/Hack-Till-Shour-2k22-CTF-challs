#!/usr/bin/python3

from pwn import *

ALPHA = '0123456789ABCDEF'
COLOR_LESS = '31'
COLOR_EQUAL = '32'
COLOR_GREATER = '34'

def compare(x):
    if COLOR_LESS in x :
        return 'l'
    elif COLOR_EQUAL in x :
        return 'e'
    else:
        return 'g'

#opening connection:
#conn = remote('programming.ctf.shellmates.club',1400)
conn = process("./chall.py")

class bins:
    def __init__(self):
        self.inf = 0 
        self.sup = len(ALPHA)-1
        self.curr = None
        self.valid = False
        self.update()

    def update(self):
        self.curr = (self.inf+self.sup)//2


length = 10

BINS = [bins() for i in range(length)]

conn.recvuntil("10\n")

while True:
    cond = "".join(ALPHA[b.curr] for b in BINS)
    conn.sendline(cond)
    try : 
        potential_flag = str(conn.recvuntil("|\n----------------------------------------\n"))
    except : 
        print(conn.recvline())
        exit()    
    result = [compare(i) for i in potential_flag.split('\\n')[1].split('|')[1:-1]]
    for res,b in zip(result,BINS):
        if res == "g":
            b.sup = b.curr-1
        elif res == "l":
            b.inf = b.curr+1
        else:
            b.valid = True
        b.update()