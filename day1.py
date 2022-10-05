# -*- coding: utf-8 -*-
"""
@author: Fouad
"""

import numpy as np

file_np = np.loadtxt('day1_data.txt')
print(file_np)

file_diff = np.diff(file_np)

increasing = file_diff[file_diff>0]

print(len(increasing))




# counter=0
# for i, val in enumerate(file_diff):
#     if file_diff[i] > file_diff[i]:
#         counter += 1
# print(counter)
