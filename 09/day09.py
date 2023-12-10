#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:11:51 2023

@author: ales
"""

import numpy as np

with open('input.txt', mode='r') as f:
    data = [[int(s) for s in l.strip().split(' ')] for l in f.readlines()]

# part 1
all_lines = []
extraps = []
for row in data:
    lines = [np.array(row)]
    while len(set(lines[-1])) > 1:
        lines.append(np.diff(lines[-1]))
    all_lines.append(lines)
    extraps.append(sum([l[-1] for l in lines]))

print(sum(extraps))

# part 2
extraps_prev = []

for lines in all_lines:
    diff = 0
    n = 0
    for i in range(len(lines)-1, -1, -1):
        n = lines[i][0] - diff
        diff = n
    extraps_prev.append(n)

print(sum(extraps_prev))