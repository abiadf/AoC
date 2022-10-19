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
command_int = list( map(int, command_np) )

# command_np2 = np.array(list(map(np.int_, command_np)))
# command_np2 = command_np.astype(int)
# print(type(command_np2))

ok = list( map(sum, zip(*command_int)) ) 






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