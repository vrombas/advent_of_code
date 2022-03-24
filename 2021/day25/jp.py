# forked from Jonathan Paulson's Submission for Day 25
# the runtime is simliar to my code, which takes 7+ seconds to run


# !/usr/bin/python3
import sys
from time import time
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque
from copy import deepcopy

#submit(len(G), part="a", day=25, year=2021)

G = []
for line in open("input.txt", 'r').read().split("\n"):
    G.append([c for c in line])

start_time = time()
R = len(G)
C = len(G[0])

t = 0
while True:
    t += 1
    moved = False
    G2 = [[G[r][c] for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            if G[r][c] == '>':
                if G[r][(c+1)%C] == '.':
                    moved = True
                    G2[r][(c+1)%C] = '>'
                    G2[r][c] = '.'
    G3 = [[G2[r][c] for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            if G2[r][c] == 'v' and G2[(r+1)%R][c] == '.':
                moved = True
                G3[(r+1)%R][c] = 'v'
                G3[r][c] = '.'
    if not moved:
        print(t)
        print(time() - start_time)
        sys.exit(0)
    G = G3

