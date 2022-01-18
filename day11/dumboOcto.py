# Time: 1hr 15min
# PartOne: 1hr 5min
# PartTwo: 10min
import copy


def partTwo(input):
    matrix = input
    sizeOfMatrix = (len(matrix[0]) * len(matrix))
    R = len(matrix)
    C = len(matrix[0])

    i = 0
    while True:
        i += 1
        # print(f'Iteration: {i}')
        # printMatrix(matrix)

        # iteration without flashing
        for x in range(R):
            for y in range(C):
                matrix[x][y] += 1

        # flash all octopuses here
        for x in range(R):
            for y in range(C):
                if matrix[x][y] > 9:
                    increaseAdj(matrix, x, y)
                    
        if sum([x.count(0) for x in matrix]) == sizeOfMatrix:
            return i


def partOne(input, t):
    matrix = input
    countFlashes = 0
    R = len(matrix)
    C = len(matrix[0])

    for i in range(t):
        # print(f'Iteration: {i+1}')
        # printMatrix(matrix)

        # iteration without flashing
        for x in range(R):
            for y in range(C):
                matrix[x][y] += 1

        # flash all octopuses here
        for x in range(R):
            for y in range(C):
                if matrix[x][y] > 9:
                    increaseAdj(matrix, x, y)

        # print(sum([x.count(0) for x in matrix]))
        countFlashes += sum([x.count(0) for x in matrix])

    return countFlashes


def increaseAdj(matrix, x, y):
    matrix[x][y] = 0
    R = len(matrix)
    C = len(matrix[0])

    for dx in range(-1, 2):
        for dy in range(-1 , 2):
            xx = x + dx
            yy = y + dy
            if 0<=xx<R and 0<=yy<C and matrix[xx][yy] != 0:
                matrix[xx][yy] += 1

                if matrix[xx][yy] > 9:
                    increaseAdj(matrix, xx, yy)


def printMatrix(matrix):
    for x in matrix:
        line = ""
        for y in x:
            line += str(y)
        print(line)
    print("-================-")


input = []
for x in open("input.txt", 'r'):
    x = x.rstrip("\n")
    line = []
    for y in x:
        line.append(int(y))
    input.append(line)

input2 =  copy.deepcopy(input)
# different object input since each function modifies grid
print(f'Part One: {partOne(input, 100)}')
print(f'Part Two: {partTwo(input2)}')