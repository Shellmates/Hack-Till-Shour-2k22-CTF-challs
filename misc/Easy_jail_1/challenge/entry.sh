#!/bin/sh

arg=""
while :; do
	printf "Input: "
	read arg
	echo $arg | ./script.py
done
