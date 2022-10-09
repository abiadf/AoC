# -*- coding: utf-8 -*-
"""
@author: Fouad
"""

import numpy as np


command = []

with open('day2_data.txt') as l:
    for lines in l.readlines():
        command[lines] = lines
        
print(command)




