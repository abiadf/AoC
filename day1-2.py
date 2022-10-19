# -*- coding: utf-8 -*-
"""
@author: Fouad
"""

import numpy as np

file_np = np.loadtxt('day1_data.txt')

triplets = np.zeros([2000-2])

for i, val in enumerate(file_np):
    if i < 1998:
        triplets[i] = np.sum(file_np[i:i+3])

triplets_diff = np.diff(triplets)
increasing = triplets_diff[triplets_diff > 0]

print(len(increasing) )
