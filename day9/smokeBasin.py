import queue
import heapq

# Time: 1hr 4min
# Part 1: 30min
# Part 2: 34min

def basin(matrix):
    basinSizes = []
    lowPoints = []
    # first get all lowPoints in matrix
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if isLowPoint(matrix, x, y):
                lowPoints.append([x, y])

    # calculate size of each Basin using BFS
    for lowPoint in lowPoints:
        someQueue = queue.Queue(0)
        visited = [lowPoint]
        someQueue.put(lowPoint)

        while someQueue.qsize() > 0:
            coordinates = someQueue.get()
            for neighbor in getNeighbor(coordinates):
                if neighbor not in visited:
                    visited.append(neighbor)
                    someQueue.put(neighbor)

        heapq.heappush(basinSizes, len(visited))

    productOfSizes = 1
    for basinSize in heapq.nlargest(3, basinSizes):
        productOfSizes *= basinSize

    return productOfSizes


def getNeighbor(coordinates):
    neighborList = []
    x = coordinates[0]
    y = coordinates[1]

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:   # removing itself from check
                continue
            if (j == -1 or j == 1) and i != 0:  # removing corners from check\
                continue
            if (x+i >= 0) and (x+i < len(matrix)) and \
                    (y+j >= 0) and (y+j < len(matrix[0])):
                if matrix[x][y] < matrix[x + i][y + j] != 9:
                    neighborList.append([x+ i, y + j])

    return neighborList


def sumLowPoints(matrix):
    sumRisk = 0
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if isLowPoint(matrix, x, y):
                riskLevel = matrix[x][y] + 1
                sumRisk += riskLevel
    return sumRisk


def isLowPoint(matrix, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:   # dont check x,y
                continue
            if (j == -1 or j == 1) and i != 0:  # dont check corners
                continue

            if (x+i >= 0) and (x+i < len(matrix)) and \
                    (y+j >= 0) and (y+j < len(matrix[0])):
                if matrix[x][y] >= matrix[x+i][y+j]:
                    return False

    return True


matrix = []
f = open("input.txt", 'r')
for line in f:
    matrix.append([int(x) for x in line.rstrip("\n")])
f.close()

print(sumLowPoints(matrix))
print(basin(matrix))