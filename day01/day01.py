# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:23:32 2023

@author: ap
"""

with open('input.txt', mode='r') as f:
    data = [l.strip() for l in f.readlines()]

# part 1
digits = list('0123456789')

numbers = [int(''.join([dgs[0], dgs[-1]])) for dgs in [[c for c in l if c in digits] for l in data]]

total = sum(numbers)

print(total)

# part 2
digits_1 = {d: int(d) for d in digits}
digits_2 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine':9}
digits_all = {**digits_1, **digits_2}

def list_digits(line, digits):               
    return [digits[d] for i in range(len(line)) for d in digits if line[i:].startswith(d)]
                
numbers = [10*dgs[0]+dgs[-1] for dgs in [list_digits(l, digits_all) for l in data] if len(dgs) > 0]

total = sum(numbers)
print(total)
