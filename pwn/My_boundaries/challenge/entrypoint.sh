#!/bin/sh

socat -d -T60 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody EXEC:"./challenge",stderr
