#!/bin/sh
TIMEOUT=300
PORT=1337
EXEC="../challenge/script.py"
USER="ctf"

socat -dd -T $TIMEOUT tcp-l:$PORT,reuseaddr,fork,keepalive exec:$EXEC
