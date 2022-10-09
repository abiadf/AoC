# -*- coding: utf-8 -*-
"""
@author: Fouad
"""

command = []
with open('day2_data.txt') as l:
    for lines in l.readlines():
        command.append(lines[:-1]) #removes last character: \n
        
aim    = 0
depth  = 0
forward= 0

for i,val in enumerate(command):
    if val[0] == 'f':
        forward += int(val[-1])
        depth   += aim * int(val[-1])

    elif val[0]=='u':
        aim -= int(val[-1])

    elif val[0]=='d':
        aim += int(val[-1])


print(depth, forward)
print(depth* forward)

