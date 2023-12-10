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

with open('test.txt', mode='r') as f:
    data = [list(l.strip()) for l in f.readlines()]
    
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

def winding(line, pt):
    a = sub(pt, line[0])
    b = sub(pt, line[1])
    v = a[0]*b[1] - a[1]*b[0]
    if v < 0:
        return -1
    if v > 0:
        return 1
    return 0


def horz_cross(r, c, line):
    if line[0][1] == r and line[1][1] == r:
        return False
    if line[0][1] >= r and line[1][1] <= r and line[0][0] >= c and line[1][0] >=c:
        return True
    return False

grid = np.zeros((n_r, n_c))

n_l = len(loop)
segments = [(loop[i], loop[(i+1) % n_l]) for i in range(n_l)]


for r in range(n_r):
    for c in range(n_c):
        for i in range(len(loop) - 1):
            line = loop[i:i+2]
            if horz_cross(r, c, line):
                print(r, line)
                grid[r, c] += winding(line, (r, c))
        print()