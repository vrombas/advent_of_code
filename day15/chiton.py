from collections import deque
from queue import PriorityQueue
import heapq


G = []
for line in open("test.txt", 'r').read().split("\n"):
    G.append([int(c) for c in line])

R = len(G)
C = len(G[0])

def part1(G):
    # need to use uniform cost search instead
    start = (0, 0, 0) # risk, x, y, path
    visited = {(0, 0)}
    Q = PriorityQueue()
    Q.put(start)

    while Q.qsize() > 0:
        print(Q)
        risk, x, y = Q.get()
        print(f'{x}, {y}, cur risk: {risk}')
        if (x==R-1 and y == C-1):
            print(risk)
            return risk

        for xx, yy in getNeighbors(x,y):
            if (xx, yy) not in visited:
                print(f'{x}, {y} -> {xx}, {yy}, cur risk: {risk}, new risk: {G[xx][yy] + risk}')
                visited.add((xx, yy))
                Q.put((G[xx][yy] + risk, xx, yy))

    return None


def getNeighbors(x,y):
    neighbors = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y
        if (0<=xx<R and 0<=yy<C):
            neighbors.append((xx, yy))
    return neighbors

print(part1(G))