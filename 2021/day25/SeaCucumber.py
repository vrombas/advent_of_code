# runtime on m1: 7s
# runtime on i5 7500: 3s

from time import time


M = []
for line in open("input.txt", 'r').read().split("\n"):
    M.append([c for c in line])

start_time = time()
R = len(M)
C = len(M[0])
# print(M)

change = True
cnt = 0

# print(F"Step: {cnt}")
# for line in M:
#     print("".join(line))
# print()

while change:
    newM = [[M[r][c] for c in range(C)] for r in range(R)]
    change = False
    cnt += 1
    for r in range(R):
        for c in range(C):
            if M[r][c] == ">":
                dc = (c + 1) % C
                if M[r][dc] == ".":
                    newM[r][c], newM[r][dc] = newM[r][dc], newM[r][c]
                    change = True

    M = newM
    newM = [[M[r][c] for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            if M[r][c] == "v":
                dr = (r + 1) % R
                if M[dr][c] == ".":
                    newM[r][c], newM[dr][c] = newM[dr][c], newM[r][c]
                    change = True

    M = newM

    # print(F"Step: {cnt}")
    # for line in M:
    #     print("".join(line))
    # print()
print(time() - start_time)
print(F"Step: {cnt}")
