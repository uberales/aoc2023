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
            return d0 + i - s0
    return i        

locations = []
for s in seeds:
    i = s
    for mn in map_names:
        i = resolve(mn, i)
    locations.append(i)
    
print(min(locations))

# part 2


seed_ranges = [(seeds[i], seeds[i]+seeds[i+1] - 1) for i in range(0, len(seeds), 2)]

def split(rng_s, rng_u):
    to_map = []
    unmapped = []
    
    if rng_u[1] < rng_s[0]:
        unmapped.append(rng_u)
    elif rng_u[0] < rng_s[0] and rng_u[1] <= rng_s[1]:
        unmapped.append((rng_u[0], rng_s[0] - 1))
        to_map.append((rng_s[0], rng_u[1]))
    elif rng_u[0] < rng_s[0] and rng_u[1] > rng_s[1]:
        unmapped.append((rng_u[0], rng_s[0] - 1))
        to_map.append(rng_s)
        unmapped.append((rng_s[1]+1, rng_u[1]))
    elif rng_u[0] >= rng_s[0] and rng_u[1] <= rng_s[1]:
        to_map.append(rng_u)
    elif rng_u[0] < rng_s[1] and rng_u[1] > rng_s[1]:
        to_map.append((rng_u[0], rng_s[1]))
        unmapped.append((rng_s[1]+1, rng_u[1]))
    elif rng_u[0] > rng_s[1]:
        unmapped.append(rng_u)
        
    return to_map, unmapped

def resolve_ranges(map_name, range_list):
    def map_range(r, d0, s0):
        return (d0 + r[0] - s0, d0 + r[1] - s0)
    
    mapped = []
    unmapped = range_list
    for d0, s0, l in map_def[map_name]:
        rng_s = (s0, s0 + l - 1)
        um_next = []
        for rng_u in unmapped:
            to_map, um_part = split(rng_s, rng_u)
            um_next.extend(um_part)
            
            for rng in to_map:
                rng_1 = map_range(rng, d0, s0)
                mapped.append(rng_1)
            
        unmapped = um_next
    
    return [*mapped, *unmapped]

loc_ranges = []
for sr in seed_ranges:
    rl = [sr]
    for mn in map_names:
        rl = resolve_ranges(mn, rl)
    loc_ranges.extend(rl)
    
print(min([r[0] for r in loc_ranges]))

