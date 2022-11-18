# -*- coding: utf-8 -*-
"""
@author: Fouad
"""

import numpy as np
import copy

def data2var(name):
    '''Convert txt file into a variable'''
    command = []
    with open(name) as l:
        for lines in l.readlines():
            ok = lines[:-1] #removes last character: \n
            command.append(ok)
    command_np = np.array(command)
    # command_dict = dict(zip(command, command_np))
    return command_np, command

def digit_count():
    '''Count the number of 1 for each digit in number length: _ _ _ _'''
    counter = num_digits * [0]
    for j in range( num_digits ):
        for i, val in enumerate(command_np):
            counter[j] += int(val[j])
    return counter

def most_common_bit(counter):
    '''Return most common bit for each digit in number: _ _ _'''
    ox_counter = num_digits * [0]
    for i, val in enumerate( ox_counter ):
        if counter[i] >= half:
            ox_counter[i] = 1
    co_counter = list(map(lambda x: 1 - x, ox_counter))
    return ox_counter, co_counter

def binary2dec(num):
    '''Converts binary number to decimal: 110 = 6'''
    num_str = list(reversed(str(num)))
    decimal = 0
    for i, val in enumerate(num_str):
        decimal += int(val) * np.power(2,int(i))
    return decimal

def element_final(command_elem, rating):
    for j, v in enumerate(rating):
        for i, val in enumerate(command_np):
            if int(val[j]) != v:
                command_elem[i] = CRIT
    
                #stop iterating when there is one remaining element
                if np.count_nonzero(command_elem == CRIT) == len(command_np)-1:
                    elem_final = command_elem
                    break
    element_crit = elem_final[ elem_final != CRIT ] [0] #keep first element
    return element_crit

# def co_final():
#     for j, v in enumerate(co_rating):
#         for i, val in enumerate(command_np):
#             if int(val[j]) != v:
#                 command_CO[i] = CRIT
                
#                 #stop iterating when there is one remaining element
#                 if np.count_nonzero(command_CO == CRIT) == len(command_np)-1:
#                     co_final = command_CO
#                     break
#     co_crit = co_final[ co_final != CRIT ] [0] #keep first element
#     return co_crit

# %% Finding the most common element

NAME = 'data3.txt' #name of text file
command_np, command = data2var(NAME) #convert txt to variable
num_digits = len( command_np[0] ) # how many digits are there
half = len(command)/2

count_ones = digit_count()
ox_rating, co_rating = most_common_bit(count_ones)

command_OX = copy.deepcopy(command_np) #oxygen copy
command_CO = copy.deepcopy(command_np) #carbon copy

CRIT = '.' #replace value when criterion is not met

ox_crit = element_final(command_OX, ox_rating)
co_crit = element_final(command_CO, co_rating)

print(ox_crit)
print(co_crit)

ox_dec = binary2dec(ox_crit)
co_dec = binary2dec(co_crit)
ok3 = ox_dec * co_dec
print(ok3)
