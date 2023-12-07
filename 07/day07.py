#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:27:31 2023

@author: podolnik
"""

from functools import cmp_to_key

with open('input.txt', mode='r') as f:
    lines = [l.strip().split(' ') for l in f.readlines()]

# part 1

def comp_val(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

class Hand:
    cards_types = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
   
    @staticmethod
    def calculate_rank(cards):
        uniques = set(cards)
        counts = {i: 0 for i in range(1, 6)}
        for u in uniques:
            counts[cards.count(u)] += 1
            
        hand_rank = 6
        if counts[5] == 1:
            hand_rank = 0
        elif counts[4] == 1:
            hand_rank = 1
        elif counts[3] == 1 and counts[2] == 1:
            hand_rank = 2
        elif counts[3] == 1:
            hand_rank = 3
        elif counts[2] == 2:
            hand_rank = 4
        elif counts[2] == 1:
            hand_rank = 5
                
        return hand_rank
           
    def rank(self):
        return Hand.calculate_rank(self.cards)
        
    def crit_secondary(self, other):
        cv = 0
        for c1, c2 in zip(self.cards, other.cards):
            i1 = self.cards_types.index(c1)
            i2 = self.cards_types.index(c2)
            cv = comp_val(i1, i2)
            if cv != 0:
                break
        return cv
    
    def comparator(self, other):
        r1 = self.rank()
        r2 = other.rank()
        c2 = self.crit_secondary(other)
        c1 = comp_val(r1, r2)
        return c1, c2
    
    def __cmp__(self, other):
        cmp = self.comparator(other)
        if cmp[0] == 0:
            return cmp[1]
        else:
            return cmp[0]
        
    def __lt__(self, other):
        return self.__cmp__(other) == 1
    
    def __gt__(self, other):
        return self.__cmp__(other) == -1
    
    def __eq__(self, other):
        return self.__cmp__(other) == 0
    
    def __repr__(self):
        return self.cards
    def __str__(self):
        return self.cards

data = [Hand(l[0], int(l[1])) for l in lines]

hands_sorted = sorted(data)
winnings = [(i+1) * hand.bid for i, hand in enumerate(hands_sorted)]
print(sum(winnings))

# part 2

class JokerHand(Hand):
    cards_types = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        
    def rank(self):
        candidates = [self.cards]
        if 'J' in self.cards:
            uniques = set(self.cards.replace('J', ''))
            for u in uniques:
                candidates.append(self.cards.replace('J', u))
        return min([Hand.calculate_rank(cards) for cards in candidates])
            
       

data = [JokerHand(l[0], int(l[1])) for l in lines]

hands_sorted = sorted(data)
winnings = [(i+1) * hand.bid for i, hand in enumerate(hands_sorted)]
print(sum(winnings))




