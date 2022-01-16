import queue
import heapq

# Time: 1hr 9min
# Part 1: 30min
# Part 2: 39min

def basin(matrix):
    basinSizes = []
    lowPoints = []
    # first get all lowPoints in matrix
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if isLowPoint(matrix, x, y):
                lowPoints.append([x, y])

    # calculate size of each Basin using BFS
    for lowPoint in lowPoints:
        Q = queue.Queue(0)
        visited = [lowPoint]
        Q.put(lowPoint)

        while Q.qsize() > 0:
            coordinates = Q.get()
            for neighbor in getNeighbor(coordinates):
                if neighbor not in visited:
                    visited.append(neighbor)
                    Q.put(neighbor)

        heapq.heappush(basinSizes, len(visited))

    productOfSizes = 1
    for basinSize in heapq.nlargest(3, basinSizes):
        productOfSizes *= basinSize

    return productOfSizes


def getNeighbor(coordinates):
    neighborList = []
    x = coordinates[0]
    y = coordinates[1]

    delta_i = [-1, 0, 1, 0]
    delta_j = [0, -1, 0, 1]

    for d in range(4):
        di = x + delta_i[d]
        dj = y + delta_j[d]
        if 0<=di<len(matrix) and 0<=dj<len(matrix[0]) and matrix[x][y] < matrix[di][dj] != 9:
            neighborList.append([di, dj])

    return neighborList


def sumRiskPoints(matrix):
    sumRisk = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if isLowPoint(matrix, x, y):
                riskLevel = matrix[x][y] + 1
                sumRisk += riskLevel
    return sumRisk


def isLowPoint(matrix, x, y):
    delta_i = [-1, 0, 1, 0]
    delta_j = [0, -1, 0, 1]

    for d in range(4):
        di = x + delta_i[d]
        dj = y + delta_j[d]
        if 0 <=di<len(matrix) and 0<=dj<len(matrix[0]) and matrix[x][y] >= matrix[di][dj]:
            return False

    return True


matrix = []
f = open("input.txt", 'r')
for line in f:
    matrix.append([int(x) for x in line.rstrip("\n")])
f.close()

print(sumRiskPoints(matrix))
print(basin(matrix))
