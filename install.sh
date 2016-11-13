#!/bin/bash

if [ $# -ne 1 ]; then
    echo $0: usage: ./install.sh gamename
    exit 1
fi

gamename=$1

files=("${gamename}/main.py")

for i in "${files[@]}"; do
    ufs put $i
done
