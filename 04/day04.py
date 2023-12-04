#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:00:25 2023

@author: podolnik
"""

def l2d(line):
    line = line.strip()
    l_prev = len(line)
    while True:
        line = line.replace('  ', ' ')
        if l_prev == len(line):
            break
        l_prev = len(line)
        
    card, nums = line.split(': ')
    no = int(card.split(' ')[-1])
    draw = set(map(int, nums.split(' | ')[0].split(' ')))
    tips = set(map(int, nums.split(' | ')[1].split(' ')))
    return no, draw, tips

with open('input.txt', mode='r') as f:
    data = [l2d(l) for l in f.readlines()]

# part 1
matches = [card[1].intersection(card[2]) for card in data]
pts = [2**(len(m) - 1) for m in matches if len(m) > 0]

print(sum(pts))

# part 2
multiplicity = [1 for _ in data]
for i in range(len(data)):
    m = matches[i]
    mul = multiplicity[i]
    for j in range(len(m)):
        multiplicity[i+j+1] += mul

print(sum(multiplicity))