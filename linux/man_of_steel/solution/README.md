# Challenge name

## Write-up

- like the description said be a good man when you connect to the server we see the flag file read it's content and it say `get some help ?`
- with this information we read the manual of the flag :
```
$ man flag

man(4)                                flag man page                               man(4)

NAME
       flag man page

DESCRIPTION
       emmm! maybe not here but you are close

SEE ALSO
       look for sections

AUTHOR
       1m4D

1.0 
```
- we look for the man section and the fourth section dedicated for special files so we read the fourth section of the manual:
```
$ man 4 flag

man(4)                                flag man page                               man(4)

NAME
       flag man page

DESCRIPTION
       congratz here is your flag: shellmates{Man_p4ge5_C4n_B3_Us3Fu1}

OPTIONS
       no option

AUTHOR
       1m4D

1.0  
```

## Flag
`shellmates{Man_p4ge_C4n_B3_Us3Fu1}`
