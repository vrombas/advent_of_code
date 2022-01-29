from collections import deque, defaultdict, Counter
steps = 10
s, pairing = open("input.txt", 'r').read().split("\n\n")

rules = {}
# print(s)
for line in pairing.split("\n"):
    p1, p2 = line.split(" -> ")
    rules[p1] = p2

for _ in range(steps):
    s_new = ""
    for i in range(len(s)):
        s_new += s[i]
        if i+1 < len(s): # takes care of adding s[-1]
            s_new += rules.get(s[i] + s[i+1], "")
    s = s_new
    # print(s)

count = Counter(s)
print(max(count.values()) - min(count.values()))
