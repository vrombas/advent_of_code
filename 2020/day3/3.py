M = []

for line in open("input.txt"):
    M.append([c for c in line.strip()])


R = len(M)
C = len(M[0])

DR = [1, 1, 1, 1, 2]
DC = [1, 3, 5, 7, 1]

ans = 1

for i in range(len(DR)):
    dr = DR[i]
    dc = DC[i]
    trees = 0

    r = dr
    c = dc

    while r < R:
        if M[r%R][c%C] == "#":
            trees += 1
        r += dr
        c += dc 

    print(trees)
    ans *= trees

print(ans)
