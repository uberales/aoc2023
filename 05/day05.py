#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:04:13 2023

@author: podolnik
"""

map_names = [
    'seed-to-soil', 
    'soil-to-fertilizer', 
    'fertilizer-to-water', 
    'water-to-light', 
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location'
    ]

map_def = {mn: [] for mn in map_names}              
seeds = []

with open('input.txt', mode='r') as f:
    mn = None
    buffer = []
    for l in f.readlines():
        l = l.strip()
        
        if l.startswith('seeds:'):
            seeds = [int(s) for s in l[7:].split(' ')]
        elif len(l) == 0:
            mn = None
        elif ' ' in l and l.split(' ')[0] in map_names:
            mn = l.split(' ')[0]
        elif mn is not None:
            map_def[mn].append([int(s) for s in l.split(' ')])

# part 1

def resolve(map_name, i):
    for d0, s0, l in map_def[map_name]:
        if i >= s0 and i < s0 + l:
            d = i - s0
            return d0 + d
    return i        

locations = []
for s in seeds:
    i = s
    for mn in map_names:
        i = resolve(mn, i)
    locations.append(i)
    
print(min(locations))

# part 2

# tbd

for i in range(0, len(seeds), 2):
    print(seeds[i+1])
        