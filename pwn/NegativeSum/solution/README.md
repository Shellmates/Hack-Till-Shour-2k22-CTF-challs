# NegativeSum

## Write-up

- In this challenge we have an integer overflow happening in the instruction ``short result= a+b`` in the [challenge.c](src/chellenge.c)
- when we pass a small values it will not change anything but when we pass big values, values that passes the SHORT_MAX=32767 (0x7FFF in hex) we make an overflow and the counting begin from the lowest values SHORT_MIN=-32768 (-8000 in hex) so the value will be negative
- To calculate the result of the overflow we use this formula: ``Overflow_result=input-65536``
- So we have ``-1337=(a+b)-65536`` <==> ``a+b=64199``
- All possible combination of a and b that gives us ``a+b=64199`` will be a solution, ex: (a,b)=(32767,31432)
```
~ nc localhost 1337
Welcome to the NegativeSum challenge
a=32767
b=31432
Congrats Here is your flag: 
shellmates{1_10v3_1nt3ger_0v3rF10w}
```
## Flag
`shellmates{1_10v3_1nt3ger_0v3rF10w}`
