# Time: 1hr 15min
# PartOne: 1hr 5min
# PartTwo: 10min

def partTwo(input):
    matrix = input
    sizeOfMatrix = (len(matrix[0]) * len(matrix))

    i = 0
    while(True):
        i += 1
        # print(f'Iteration: {i}')
        # printMatrix(matrix)

        # iteration without flashing
        for x in range(len(input)):
            for y in range(len(input[0])):
                matrix[x][y] += 1

        # flash all octopi here
        for x in range(len(input)):
            for y in range(len(input[0])):
                if matrix[x][y] > 9:
                    increaseAdj(matrix, x, y)
        if sum([x.count(0) for x in matrix]) == sizeOfMatrix:
            return i


def partOne(input, n):
    matrix = input
    countFlashes = 0
    for i in range(n):
        # print(f'Iteration: {i+1}')
        # printMatrix(matrix)

        # iteration without flashing
        for x in range(len(input)):
            for y in range(len(input[0])):
                matrix[x][y] += 1

        # flash all octopi here
        for x in range(len(input)):
            for y in range(len(input[0])):
                if matrix[x][y] > 9:
                    increaseAdj(matrix, x, y)
        print(sum([x.count(0) for x in matrix]))
        countFlashes += sum([x.count(0) for x in matrix])
    return countFlashes

def increaseAdj(matrix, x, y):
    matrix[x][y] = 0
    for dx in range(-1, 2):
        for dy in range(-1 , 2):
            if 0<=x+dx<len(matrix) and 0<=y+dy<len(matrix[0]) and not (dx == 0 and dy == 0):
                if matrix[x+dx][y+dy] > 0:
                    matrix[x+dx][y+dy] += 1

                    if matrix[x+dx][y+dy] > 9:
                        increaseAdj(matrix, x+dx, y+dy)


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

# print(partOne(input, 100))
print(partTwo(input))