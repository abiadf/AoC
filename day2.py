# -*- coding: utf-8 -*-
"""
@author: Fouad
"""

import numpy as np

file_np = np.loadtxt('day1_data.txt')
# print(file_np)

sum_array = np.array([1])
np.append(sum_array, [2])#, axis=0)
print(sum_array)

# for i, val in enumerate(file_np):
#     if i <= len(file_np)-3:
#         sum_3 = file_np[i] + file_np[i+1] + file_np[i+2]
#         np.append(sum_array, sum_3)

print(sum_array)

