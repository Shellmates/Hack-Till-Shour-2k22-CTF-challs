#!/usr/bin/env python3
import random
from termcolor import colored

FLAG = "shellmates{W0rDl3_y90u3edwji9300h}"
color = {1: "blue", 0: "green", -1: "red"}

CHARS = "0123456789ABCDEF"

def print_wordle(_input, word):
    correct_indexes = []
    for i in range(len(word)):
        if word[i] == _input[i]:
            correct_indexes.append(0)
        elif word[i] > _input[i]:
            correct_indexes.append(-1)
        else:
            correct_indexes.append(1)

    print((len(word)) * "----")
    print(
        "| "
        + " | ".join([colored(i, color[j]) for i, j in zip(_input, correct_indexes)])
        + " |"
    )
    print((len(word)) * "----")


def main():
    print(
        "Hello Hackers welcome to my wordle game.\nI have a word in mind and you have to guess it (it's written in hex)\nI'll help you:\nred for lower, blue for higher, length is 10"
    )
    words = open("wordlist.txt").readlines()
    random_word = (words[random.randint(0, len(words))]).strip()
    LEN = len(random_word)
    count = 0
    MAX_TRIES = 5
    found = False
    while not found and count < MAX_TRIES:
        _input = input()
        if len(_input) != LEN:
            print("wrong length")
            continue
        if any(char not in CHARS for char in _input ):
            print(f"Not allowed. We only accept : {CHARS}")
            continue
        count += 1
        if _input == random_word:
            print(FLAG)
            found = True
        else:
            print_wordle(_input, random_word)


if __name__ == "__main__":
    main()
