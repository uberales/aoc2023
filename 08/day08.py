#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:58:41 2023

@author: podolnik
"""

import re

with open('test.txt', mode='r') as f:
    instructions = list(f.readline().strip())
    txt = f.read()
    matches = re.findall('([0-9A-Z]+)\s=\s\(([0-9A-Z]+), ([0-9A-Z]+)\)', txt)
    nodes = {m[0]: {'L': m[1], 'R': m[2]} for m in matches}

# part 1
n_i = len(instructions)
def iterate(n_from, n_to, offset=0):
    n = n_from
    i = offset
    while True:
        d = instructions[i % n_i]
        n = nodes[n][d]
        i += 1
        print(n, i)
        if n.endswith(n_to):
            break
    return i-offset, n

if 'AAA' in nodes:
    i, n_last = iterate('AAA', 'ZZZ')
else:
    i, n_last = iterate('11A', '11Z')
print(i)

# part 2

def check_loop(n_from):
    n = n_from
    i = 0
    seen = {(n, 0): 0}
    while True:
        d = instructions[i % n_i]
        n = nodes[n][d]
        i += 1
        if (n, i % n_i) in seen:
            break
        seen[(n, i % n_i)] = i
    return n, seen[(n, i % n_i)], i

nodes_start = [n for n in nodes if n.endswith('A')]
nodes_loops = {n: check_loop(n) for n in nodes_start}
nodes_periods = {n: iterate(nodes_loops[n][0], 'Z', offset=nodes_loops[n][1])[0] for n in nodes_start}
nodes_end = {n: iterate(n, 'Z') for n in nodes_start}

min_vals = [nodes_loops[n][1] for n in nodes_start]
deltas = [nodes_periods[n] for n in nodes_periods]

i = 0
while True:
    pos = [min_vals[k] + i * d for k, d in enumerate(deltas)]
    if len(set(pos)) == 1 and i > 0:
        break
    i += 1
print(i)
