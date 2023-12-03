#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:48:26 2023

@author: ales
"""

with open('input.txt', mode='r') as f:
    data = [l.strip() for l in f.readlines()]
    
# part 1
    
def is_symbol(c):
    return c not in '0123456789.'

numbers = []
n_r = len(data)
n_c = len(data[0])

for r in range(n_r):
    row = data[r]
    n = ''
    c_min = None
    c_max = None
    for c in range(n_c):
        char = row[c]
        if char.isdigit():
            if n == '':
                c_min = c
                c_max = c
            else:
                c_max = c
            n += char
        else:
            if n != '':
                numbers.append((int(n), r, c_min, c_max))
                n = ''
    if n != '':
        numbers.append((int(n), r, c_min, c_max))
        
def get_nb(r, c):
    if r >= 0 and r < n_r and c >= 0 and c < n_c:
        return data[r][c]
    return '.'
    
def get_neighbors(num):
    n, r, c_min, c_max = num
    candidates = []
    candidates.append((r, c_min-1))
    candidates.append((r, c_max+1))
    for ic in range(c_min-1, c_max+2):
        candidates.append((r-1, ic))
        candidates.append((r+1, ic))
    
    nbs = []
    for r, c in candidates:
        nb = get_nb(r, c)
        if is_symbol(nb):
            nbs.append((nb, r, c))
    
    return nbs

numbers_pts = [n[0] for n in numbers if len(get_neighbors(n)) > 0]
print(sum(numbers_pts))

# part 2

all_nbs = {n: get_neighbors(n) for n in numbers}
nb_stats = {}
for n in all_nbs:
    nbs = all_nbs[n]
    for nb in nbs:
        if nb in nb_stats:
            nb_stats[nb].append(n)
        else:
            nb_stats[nb] = [n]

ratios = [nb_stats[nb][0][0] * nb_stats[nb][1][0] for nb in nb_stats if nb[0] == '*' and len(nb_stats[nb]) == 2]
     
print(sum(ratios))
