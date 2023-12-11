#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:33:59 2023

@author: ales
"""

import numpy as np

all_dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

pipe_def = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    'S': [],
    '.': []
    }

with open('input.txt', mode='r') as f:
    data = [list(l.strip()) for l in f.readlines()]

# part 1

n_r, n_c = len(data), len(data[0])

def add(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]

def sub(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]

def validate(coords, n_r, n_c):
    valid = []
    for c in coords:
        if c[0] >= 0 and c[0] < n_r and c[1] >= 0 and c[1] < n_c:
            valid.append(c)
    return valid

graph = {}

def add_or_append(graph, k, v):
    if k not in graph:
        graph[k] = set()
    graph[k].add(v)

start = ()

for r in range(n_r):
    for c in range(n_c):
        coords = (r, c)
        p = data[r][c]
        if p == 'S':
            start = coords
        dirs = pipe_def[p]
        nbs = validate([add(coords, d) for d in dirs], n_r, n_c)
        for nb in nbs:
            add_or_append(graph, coords, nb)

start_nbs = validate([add(start, d) for d in all_dirs], n_r, n_c)

for nb in start_nbs:
    if nb in graph:
        if start in graph[nb]:
            add_or_append(graph, start, nb)
            
def trace(graph, start, d):
    seen = [start, d]
    while True:
        possible = [c for c in graph[seen[-1]] if c not in seen]
        if len(possible) == 0:
            break
        seen.append(possible[0])
    return {c: seen.index(c) for c in seen}, seen
        
traces = [trace(graph, start, d) for d in graph[start]]

loop = traces[0][1]

minima = [min([t[0][c] for t in traces]) for c in loop]
print(max(minima))

# part 2

def get_dir(loop, pt):
    if pt not in loop:
        return 0
    i = loop.index(pt)
    prv = loop[(i - 1) % len(loop)]
    nxt = loop[(i + 1) % len(loop)]
    dr = nxt[0] - prv[0]
    return dr

grid = np.zeros((n_r, n_c), dtype=int)

for r in range(n_r):
    for c in range(n_c):
        if (r, c) not in loop:
            for cx in range(c+1,n_c):
                pt = (r, cx)
                d = get_dir(loop, pt)
                grid[r, c] += d
print(np.sum(abs(grid) > 0))