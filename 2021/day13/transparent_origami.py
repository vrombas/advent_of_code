p1 = True

def partOne(input, direction):
    G = set()
    for x,y in input:
        G.add((x, y))

    first = True
    for d, v in direction:
        G2 = set() # "RuntimeError: Set changed size during iteration"
        if d == "y":
            for x,y in G:
                if (y < v):
                    G2.add((x,y))
                else:
                    # case where y==v is included here
                    G2.add((x, v-(y-v)))
        else:
            assert d == "x"
            for x,y in G:
                if (x < v):
                    G2.add((x,y))
                else:
                    G2.add((v-(x-v), y))

        G = G2
        if p1 and first:
            first = False
            print(f'Part One: {len(G)}')

    X = max(x for x,y in G)
    Y = max(y for x,y in G)
    print(f'cols: {X} rows: {Y}')

    # X is left->right and Y is up->down
    for y in range(Y+1):
        row = ""
        for x in range(X+1):
            row += "#" if (x,y) in G else " "
        print(row)
    return None

# get input
direction = []
input = []
for line in open("input.txt", 'r'):
    line = line.rstrip("\n")
    if line and line.startswith("fold"):
        line = line.split(" ")[-1]
        d, v = line.split("=")
        # print(f'd: {d}, v: {v}')
        direction.append((d, int(v)))
    elif line:
        x, y = line.split(",")
        input.append((int(x), int(y)))

print(partOne(input, direction))
