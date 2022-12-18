import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "4.in"


acc = 0

for x in open(infile):
    a, b = x.strip().split(",")

    a = a.split("-")
    b = b.split("-")
    print(a, b)

    # a.......a
    #   b..b
    if a[0] <= b[0] <= b[1] <=a[1]:
        acc += 1
        continue

    #   b.......b
    #      a..a
    if b[0] <= a[0] <=a[1] <= b[1]:
        acc += 1
        continue
    

print(acc)
