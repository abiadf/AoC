# -*- coding: utf-8 -*-
"""
@author: Fouad
"""

command = []
with open('day2_data.txt') as l:
    for lines in l.readlines():
        command.append(lines[:-1]) #removes last character: \n
        
up     = 0
down   = 0
forward= 0

for i,val in enumerate(command):
    if val[0] == 'f':
        forward += int(val[-1])
    elif val[0]=='u':
        up += int(val[-1])
    elif val[0]=='d':
        down += int(val[-1])

vertical = down - up
print(vertical, forward)
print(vertical * forward)



