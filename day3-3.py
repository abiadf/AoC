# -*- coding: utf-8 -*-
"""
@author: Fouad
"""

import numpy as np
import copy
import collections

command = []
with open('data3.txt') as l:
    # lst = [int(x) for x in l.read().split()]
    for lines in l.readlines():
        ok = lines[:-1] #removes last character: \n
        command.append(ok)
        
command_np = np.array(command)

# command_dict = dict(zip(command, command_np))
# print( command_dict)

half = len(command)/2


# %% Finding the most common element
num_digits = len(command_np[0])

counter = num_digits * [0]
for j in range( num_digits ):
    for i,val in enumerate(command_np):
        counter[j] += int(val[j])

ox_counter = num_digits * [0]
for i, val in enumerate( ox_counter ):
    if counter[i] >= half:
        ox_counter[i] = 1


command_OX = copy.deepcopy(command_np) #oxygen copy
command_CO = copy.deepcopy(command_np) #carbon copy

ox_del = 0 # number of items deleted from oxygen
co_del = 0 # number of items deleted from carbon
for j, v in enumerate(ox_counter):
    for i, val in enumerate(command_np):
        
        if int(val[j]) != v:
            command_OX[i] = 3
            ox_del += 1
        if int(val[j]) == v:
            command_CO[i] = 3
            co_del += 1



print(ox_del)
    # if ox_del == 999:
    #     print(command_OX)
    # if co_del == 999:
    #     print(command_CO)
    # break

# print(command_OX)
# print(command_CO)




# command_np2 = np.array(list(map(np.int_, command_np)))
# command_np2 = command_np.astype(int)
# print(type(command_np2))
# print( command_np2[1], command_np2[1][2] )

# ok = list( map(sum, zip(*command_int)) ) 

# for i,val in enumerate(command):
#     print(val)


# command_np2 = command_np.astype(float)
# print( type(command_n+p2), type(command_np2[0]))


# def sum_maker(digit):
    # ok = ( list( map(sum, zip(*command_np2)) ) )

#     numsum = 0 # set counter to 0
#     for i, val in enumerate(command_np):
#         numsum += int(val[digit])
#     if numsum < len(command_np)/2:
#         ox_crit = 0
#     else:
#         ox_crit = 1

#     command_ox = command_np
#     command_co = command_np
#     for i, val in enumerate(command_np.copy()):
#         if int(val[digit]) == ox_crit:
#             # command_ox.append(val)
#             np.delete(command_co, i)
#         else:
#             # command_co.append(val)
#             np.delete(command_ox, i)

#     print(command_ox, command_co)
#     return command_ox, command_co

# ox, co = sum_maker(0)