def partOne(input, n):
    matrix = input
    for i in range(n):
        for x in range(len(input)):
            for y in range(len(input[0])):
                printMatrix(matrix)
                matrix[x][y] += 1
                if  matrix[x][y] == 10:
                    increaseAdj(matrix, x, y)

def increaseAdj(matrix, x, y):
    matrix[x][y] = 0
    for dx in range(-1, 2):
        for dy in range(-1 , 2):
            if 0<=x+dx<len(matrix) and 0<=y+dy<len(matrix[0]) and not (dx == 0 and dy == 0):
                matrix[x+dx][y+dy] += 1
                if matrix[x+dx][y+dy] == 10:
                    increaseAdj(matrix, x+dx, y+dy)
    return None


def printMatrix(matrix):
    for x in matrix:
        line = ""
        for y in x:
            line += str(y)
        print(line)
    print("-================-")


input = []
for x in open("test_9s.txt", 'r'):
    x = x.rstrip("\n")
    line = []
    for y in x:
        line.append(int(y))
    input.append(line)

print(partOne(input, 10))