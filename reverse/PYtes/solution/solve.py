#!/usr/bin/env python3

from Crypto.Util.number import inverse

def dec(key, char):
	return (inverse(key,256)*char) % 256

if __name__ == '__main__':
	with open("../challenge/out.bin","rb") as f:
		out = f.read()
		for i in range(1,256):
			if bytes([dec(i,out[0])]) == b"s":

				key = i
				print(key) 
				break 
		plain = b""
		for char in out :
			plain+= bytes([dec(key,char)])

	with open("flag","wb") as f:
		f.write(plain)