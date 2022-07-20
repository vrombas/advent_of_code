import math

mx = 0

input = [x.strip() for x in open("input.txt", 'r')]

# input = ["BFFFBBFRRR"]
seats = []

for line in input:
    rl, rr = 0, 127
    cl, cr = 0, 7
    for c in line:
        if c == "F":
            rr = math.floor((rr + rl)/2)
        elif c == "B":
            rl = math.ceil((rr + rl)/2)
        elif c == "R":
            cl = math.ceil((cr + cl)/2)
        elif c == "L":
            cr = math.floor((cr + cl)/2)

    mx = max(mx, (rl * 8 + cl))
    seats.append(mx)


seats.sort()
print(seats)
seat_ans = seats[len(seats)//2]

print("seat ans")
print(seat_ans)
