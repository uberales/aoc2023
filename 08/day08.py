#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:58:41 2023

@author: podolnik
"""

import re
import numpy as np

with open('input.txt', mode='r') as f:
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
        if n.endswith(n_to):
            break
    return i-offset, n

if 'AAA' in nodes:
    i, n_last = iterate('AAA', 'ZZZ')
else:
    i, n_last = iterate('11A', '11Z')
print(i)

# part 2

nodes_start = [n for n in nodes if n.endswith('A')]
nodes_end = {n: iterate(n, 'Z') for n in nodes_start}

nodes_periods = [nodes_end[n][0] for n in nodes_end]
print(np.lcm.reduce(nodes_periods))
