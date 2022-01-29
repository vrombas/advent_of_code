from collections import deque, defaultdict, Counter
steps = 40
s, pairing = open("input.txt", 'r').read().split("\n\n")

rules = {}
for line in pairing.split("\n"):
    p1, p2 = line.split(" -> ")
    rules[p1] = p2

counter = {}
# add initial pairs
for i in range(len(s)-1):
    counter[s[i]+s[i+1]] = counter.get(s[i] + s[i+1], 0) + 1

for t in range(1, steps+1):
    temp = {}
    # NN -> (NC, CN) both with same count as NN
    for k in counter:
        temp[k[0] + rules[k]] = temp.get(k[0] + rules[k], 0) + counter[k]
        temp[rules[k] + k[1]] = temp.get(rules[k] + k[1], 0) + counter[k]

    counter = temp
    # print part1 and part2
    if t in [10, 40]:
        letter_count = {}
        for k in counter:
            # Every character appears in the first half of its pair except for the last character
            letter_count[k[0]] = letter_count.get(k[0], 0) + counter[k]
        # add 1 to count of last character, which remains unchanged from the original string
        letter_count[s[-1]] = letter_count.get(s[-1], 0) + 1

        print(f'At step {t}: {max(letter_count.values()) - min(letter_count.values())}')

# I really need to do something about my input and output for these
# switch back and forth between test.txt and input.txt have cost me so much time
