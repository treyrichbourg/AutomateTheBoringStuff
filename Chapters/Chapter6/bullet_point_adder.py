#!/usr/bin/env python3
#bullet_point_adder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

#Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):     #loop through all indexes in the "lines" list
    #lines[i] = '* ' + lines[i] #add start to each string in "lines" lsit
    lines[i] = f"* {lines[i]}"  #written as an fstring

text = '\n'.join(lines)

pyperclip.copy(text)
