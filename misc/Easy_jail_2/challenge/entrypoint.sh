#!/bin/sh

socat -dd -T300 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"./script.py",stderr
