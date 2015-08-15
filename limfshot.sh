#!/bin/bash
export i=screenshot.png
scrot $i
limf -l $i|xclip -selection clipboard
rm $i
