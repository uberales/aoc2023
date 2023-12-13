#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:34:18 2023

@author: podolnik
"""

import numpy as np

grids = []

with open('input.txt', mode='r') as f:
    buffer = []
    for l in f.readlines():
        l = l.strip().replace('#', '1').replace('.', '0')
        if len(l) == 0:
            grids.append(np.array(buffer))
            buffer = []
        else:
            buffer.append([int(s) for s in l])
    grids.append(np.array(buffer))
    
# part 1           

def check_symmetry(grid, offset, n_smudges = 0):
    n_r, n_c = np.shape(grid)
    if offset == 0:
        return False
    slice_size = min(offset, n_c - offset)
        
    left = grid[:,offset-slice_size:offset]
    right = np.fliplr(grid[:,offset:offset+slice_size])
    
    n_same = np.sum(left==right)
    return n_same == n_r * slice_size - n_smudges

sym_hor = []
sym_ver = []
for g in grids:
    g_hor = g
    c_s = [o for o in range(len(g_hor[0])) if check_symmetry(g_hor, o)]
    g_ver = g.T
    r_s = [o for o in range(len(g_ver[0])) if check_symmetry(g_ver, o)]
    sym_hor.extend(c_s)
    sym_ver.extend(r_s)
    
sol = 100 * np.sum(sym_ver) + np.sum(sym_hor)
print(sol)

# part 2

sym_hor = []
sym_ver = []
for g in grids:
    g_hor = g
    c_s = [o for o in range(len(g_hor[0])) if check_symmetry(g_hor, o, n_smudges=1)]
    g_ver = g.T
    r_s = [o for o in range(len(g_ver[0])) if check_symmetry(g_ver, o, n_smudges=1)]
    sym_hor.extend(c_s)
    sym_ver.extend(r_s)
    
sol = 100 * np.sum(sym_ver) + np.sum(sym_hor)
print(sol)
