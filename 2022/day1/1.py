import sys
infile = sys.argv[1] if len(sys.argv)>1 else 'input.txt'

elf = 0

max_elf = 0
max_cnt = 0

acc = 0

values = []

curr = []
for line in open(infile, 'r'):
    if line == "\n":
        values.append(curr)
        curr = []
        continue

    curr.append(int(line.strip()))


summed = [sum(n) for n in values]
summed.sort()

print(summed[len(summed)-3:])
print(f"Part 1: {summed[-1]}")
print(f"Part 2: {sum(summed[-3:])}")
assert False



