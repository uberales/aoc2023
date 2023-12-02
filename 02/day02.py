# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 09:55:16 2023

@author: ap
"""

def l2d(line):
    line = line.strip()
    a, b = line.split(': ')
    gid = int(a.split(' ')[-1])
    def p2r(pt):
        c = pt.split(', ')
        return {d.split(' ')[1]: int(d.split(' ')[0]) for d in c}
        
    return gid, [p2r(p) for p in b.split('; ')]
    
with open('input.txt', mode='r') as f:
    data = [l2d(l) for l in f.readlines()]
    
maxvals = {'red': 12, 'green': 13, 'blue': 14}

# part 1

ids = []

for game in data:
    possible = True
    for rnd in game[1]:
        for col in rnd:
            if rnd[col] > maxvals[col]:
                possible = False
                break
    if possible:
        ids.append(game[0])
        
print(sum(ids))

# part 2

powers = []

for game in data:
    p = {'red': 0, 'green': 0, 'blue': 0}
    for rnd in game[1]:
        for col in rnd:
            p[col] = max(p[col], rnd[col])
    pwr = p['red'] * p['green'] * p['blue']
    powers.append(pwr)
    
print(sum(powers))