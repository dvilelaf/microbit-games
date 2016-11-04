#!/bin/bash

files=("main.py")

for i in "${files[@]}"; do
    ufs put $i
done
