#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:23:23 2023

@author: podolnik
"""

import re
import numpy as np

with open('input.txt', mode='r') as f:
    txt = f.read()
    m = re.findall('\d+', txt)
    n = len(m)
    times = [int(s) for s in m[:n//2]]
    distances = [int(s) for s in m[n//2:]]

# part 1
def num_sol(t, d):
    h_0 = (t - np.sqrt(t*t - 4*d))/2 
    h_1 = (t + np.sqrt(t*t - 4*d))/2 
    
    hi_0 = max(1, np.floor(h_0 + 1).astype(int))
    hi_1 = np.ceil(h_1 - 1).astype(int)
    return hi_1 - hi_0 + 1 

h_min = [num_sol(t, d) for t, d in zip(times, distances)]
print(np.prod(h_min))

# part 2
time = int(''.join([f'{n}' for n in times]))
distance = int(''.join([f'{n}' for n in distances]))
print(num_sol(time, distance))