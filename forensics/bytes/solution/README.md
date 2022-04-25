# Bytes

## Write-up

Having a look at the bytes.txt file, we can see a list of tuples containing 2 numbers, one in decimal and the other in hex.

The challenge talks about bytes, we can figure that the solution requires reordering the bytes and writing them to a file.

Obviously the first item of the tuple contains the order, and the second is no more than the bytes itself ( written in hex make it clear )

There are multiple ways to do that, we provide below a simple easy script with python!

```python
#
all_bytes= eval(open("bytes.txt","r").read())

#empty list
l= [b"_" for i in range(len(all_bytes))]
for i in all_bytes:
	l[i[0]]=i[1].to_bytes(1,byteorder='big')


open("solution","wb").write(b"".join(l))
```

What kind of file did we get ?

```bash
$file solution
PNG image data, 605 x 32, 8-bit/color RGBA, non-interlaced
```

View the image and here is a flag!

## Flag

`shellmates{s0m3th1ng_l33t}`
