from collections import deque

G = []
for line in open("test.txt", 'r').read().split("\n"):
    G.append([int(c) for c in line])

R = len(G)
C = len(G[0])

def part1(G):

    start = (0, 0, 0) # x, y, risk
    visited = {(0,0)}
    Q = deque([start])

    ans = []
    while Q:
        x, y, risk = Q.popleft()
        if (x==R-1 and y == C-1):
            print(x, y, risk)
            ans.append(risk)

        for xx, yy in getNeighbors(x,y):
            if (xx, yy) not in visited:
                Q.append((xx, yy, G[xx][yy] + risk))
                visited.add((xx,yy))

    print(ans)
    return min(ans)



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