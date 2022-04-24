#!/usr/bin/env python3

from sys import exit

BAD = "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
Flag = "shellmates{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"

if __name__ == "__main__":
    print("---- show_variables_AAS - Everything is a service now ----\n\n")

    while True:
        var = input("Which variable you want to see --> ")
        if var == "Flag":
            print("NOOO, not that one!")
        elif var == "exit":
            exit()
        elif any(bad in var for bad in BAD):
            print("It would have been easy")
        else:
            try:
                print(eval(var))
            except:
                print("Your are trying to break my program")
