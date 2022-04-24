#!/usr/bin/env python3

import random

KEY = random.randint(1,256)

def enc(char):
	return KEY*char % 256


if __name__ == '__main__':
	with open("flag", "rb") as f :
		content = f.read()
		out = b""
		for char in content :
			out += bytes([enc(char)])
	with open("out.bin", "wb") as f :
		f.write(out)