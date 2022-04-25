# Weird PY 2 

## Write-up

In this part, we also need to output the content of the flag, but there is a blacklist. From the first look, it seems that we are only limited to letters, but since this is a blacklist and not a white list, we can search for other letters that Python accepts . 

After some research, you can find unicode characters that Python accepts and interprets and, fortunately, they are not present in the blacklist.
https://gosecure.github.io/unicode-pentester-cheatsheet/

```
Flaℊ
```


## Flag
`shellmates{Th0s3_UNIC0D3_C0mplety_Ruin3d_IT}}`
