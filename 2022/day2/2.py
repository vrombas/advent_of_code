import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "2.in"

key = [["C", "B", "A"], ["Z", "Y", "X"]]
score = [3, 2, 1]

# part 1
acc = 0
for line in open(infile):
    a, b = line.strip().split(" ")
    idx = key[1].index(b)

    if a == key[0][(idx+1)%3]:
        # win
        acc += 6 + score[idx]

    elif a == key[0][idx]:
        # tie
        acc += 3 + score[idx] 

    else:
        # loss
        acc += 0 + score[idx]


print(f"Part 1: {acc}")


# part 2
acc = 0
for line in open(infile):
    a, b = line.strip().split(" ")
    idx = key[0].index(a)

    if b == "Z":
        # win
        acc += 6 + score[(idx-1)%3]

    elif b == "Y":
        # tie
        acc += 3 + score[idx] 

    else:
        # loss
        acc += 0 + score[(idx+1)%3]


print(f"Part 2: {acc}")

