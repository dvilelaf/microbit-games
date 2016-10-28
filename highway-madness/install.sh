#!/bin/bash

files=("main.py" "animations.py" "../libraries/object.py" "../libraries/screen.py")

for i in "${files[@]}"; do
    ufs put $i
done
