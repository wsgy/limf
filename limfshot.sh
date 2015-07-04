#!/bin/bash
export i=screenshot.png
scrot $i
./limf.py -l $i|xclip -selection c
rm $i
