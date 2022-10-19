# -*- coding: utf-8 -*-
"""
@author: Fouad
"""

import numpy as np

command = []
with open('data3.txt') as l:
    for lines in l.readlines():
        command.append(lines[:-1]) #removes last character: \n        
command_np = np.array(command)

numbers = [0] * len( command_np[0] )
numsum = 0 # set counter to 0
for j,v in enumerate(numbers): # loop through numbers
    for i, val in enumerate(command_np):
        numsum += int(val[j])
    numbers[j] = numsum
    numsum = 0

lead_num = [-1] * len( command_np[0] )
lost_num = [-1] * len( command_np[0] )
for i,val in enumerate(numbers):
    if val< 500:
        lead_num[i] = str(0)
        lost_num[i] = str(1)
    else:
        lead_num[i] = str(1)
        lost_num[i] = str(0)

gamma_binary  = ''.join( lead_num )
epsilon_binary= ''.join( lost_num )
print(gamma_binary, epsilon_binary)

def binary2decimal(num):
    reverse = reversed(num)
    decimal = 0
    for i,val in enumerate(reverse):
        index = np.power(2, i) * int(val)
        decimal += index
    print(decimal)
    return decimal

gamma = binary2decimal(gamma_binary)
epsilon = binary2decimal(epsilon_binary)

power = gamma*epsilon
print(power)