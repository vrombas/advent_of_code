from queue import PriorityQueue
# Note: Could've used heapq as well (heappush & heappop)



# need to use uniform-cost search instead
def UCS(G, n_tiles):
    R = len(G)
    C = len(G[0])

    Q = PriorityQueue()
    start = (0, 0, 0) # risk, x, y
    Q.put(start)

    # data structure to hold risks (distances) of each pos
    distG = [[None for _ in range(C*n_tiles)] for _ in range(R*n_tiles)]

    while Q.qsize() > 0:
        risk, x, y = Q.get()

        # adding (x//R) because we want x + 1 for every R
        cur_risk = G[x%R][y%C] + (x//R) + (y//C)

        while cur_risk > 9:  # can't use modulo here because 18%9 = 0, we want 9
            cur_risk -= 9
        total_risk = cur_risk + risk

        if (x == R*n_tiles-1 and y == C*n_tiles-1):
            return total_risk - G[0][0]


        # or total_risk < distG[x][y] is unneeded since the PQ ensures that the node with
        # the lowest risk is searched next
        if distG[x][y] is None: # if it's never been visited
            distG[x][y] = total_risk
        else:
            continue

        # getNeighbors
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0<=xx<R*n_tiles and 0<=yy<C*n_tiles:
                Q.put((total_risk, xx, yy))

    return None


G = []
for line in open("input.txt", 'r').read().split("\n"):
    G.append([int(c) for c in line])


print(f'Part 1: {UCS(G, 1)}')
print(f'Part 2: {UCS(G, 5)}')