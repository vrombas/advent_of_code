from collections import deque
from queue import PriorityQueue
# Note: Could've used heapq as well (heappush & heappop)

# need to use uniform-cost search instead
def UCS(G):
    start = (0, 0, 0) # risk, x, y
    visited = {(0, 0)}
    Q = PriorityQueue()
    Q.put(start)

    while Q.qsize() > 0:
        risk, x, y = Q.get()
        # print(f'{x}, {y}, cur risk: {risk}')
        if (x==R-1 and y == C-1):
            return risk

        for xx, yy in getNeighbors(x,y):
            if (xx, yy) not in visited:
                # print(f'{x}, {y} -> {xx}, {yy}, cur risk: {risk}, new risk: {G[xx][yy] + risk}')
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


G = []
for line in open("input.txt", 'r').read().split("\n"):
    G.append([int(c) for c in line])

R = len(G)
C = len(G[0])
print(f'Part 1: {UCS(G)}')

G5 = []

for j in range(R*5):
    line = []
    for i in range(5):
        # for each tile
        for rr in G[j%R]:
            # for each row in original
            new_rr = (rr + i + j//R) # j should be [0, R)
            while (new_rr > 9): # can't use modulo here because 18%9 = 0, we want 9
                new_rr -=9

            line.append(new_rr)

    # print(line)
    G5.append(line)

# g = open("input5x.txt", 'w')
# for line in G5:
#     g.write("".join([str(c) for c in line]))
#     g.write("\n")

# redefinition of R and C needed for part2
R = len(G5)
C = len(G5[0])
print(f'Part 2: {UCS(G5)}')
