#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:46:02 2023

@author: podolnik
"""

import numpy as np

with open('input.txt', mode='r') as f:
    data = [list(l.strip()) for l in f.readlines()]

# part 1

n_r, n_c = len(data), len(data[0])

cols = list(range(n_c))
rows = list(range(n_r))

galaxies = []
for r in range(n_r):
    for c in range(n_c):
        if data[r][c] == '#':
            if c in cols:
                cols.pop(cols.index(c))
            if r in rows:
                rows.pop(rows.index(r))
            galaxies.append((r, c))

def expand(galaxies, q = 2):
    expanded_galaxies = []
    for g in galaxies:
        eg = g
        for ir in range(len(rows)-1, -1, -1):
            if rows[ir] < eg[0]:
                eg = (eg[0] + (ir + 1) * (q - 1), eg[1])
                break
        for ic in range(len(cols)-1, -1, -1):
            if cols[ic] < eg[1]:
                eg = (eg[0], eg[1] + (ic + 1) * (q - 1))
                break
        expanded_galaxies.append(eg)
    return expanded_galaxies

def get_distances(galaxies):
    distances = {}
    for eg1 in galaxies:
        for eg2 in galaxies:
            distances[(eg1, eg2)] = np.abs(eg1[0] - eg2[0]) + np.abs(eg1[1] - eg2[1])
    return distances

distances = get_distances(expand(galaxies))
               
print(sum(distances.values()) // 2)

# part 2

distances = get_distances(expand(galaxies, q = 1000000))
               
print(sum(distances.values()) // 2)
