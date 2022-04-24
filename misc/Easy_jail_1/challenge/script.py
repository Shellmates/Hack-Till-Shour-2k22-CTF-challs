#!/usr/bin/env python2.7

FLAG="shellmates{1npuT_FuncT1on_C4n_R34D_V4r14Bl35}"

import sys

while True :
    try:
        sys.stdout.write("Input>> ")
        sys.stdout.flush()
        exp=input()
        print exp
    except:
        sys.stdout.write("Error\n");
        sys.stdout.flush()
