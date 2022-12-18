from collections import defaultdict

parents = defaultdict(list)
contents = defaultdict(list)

for l in open("input.txt"):
    line = l.strip()
    parent, children = line.split(" contain ")
    parent = parent.rstrip("s")

    for b in children.strip(".\n").split(","):
        bag = b.strip()  # idk how to avoid this
        if bag == "no other bags":
            continue

        cnt = int(bag[:bag.find(" ")].strip())
        bag_id = bag[bag.find(" "):].strip().rstrip("s")

        # list of tuples wth cnt and bag_id
        contents[parent].append((cnt, bag_id))

        parents[bag_id].append(parent)

# print(parents)
# print(" ")
# print(bag_cnt)

for x in parents.items():
    pass

# start bfs from shiny gold bag
query = "shiny gold bag" 
visited = set()
Q = [query]

while Q:
    child = Q.pop()
    for p in parents[child]:
        if p not in visited:
            Q.append(p)
        visited.add(p)

print("part 1")
print(len(visited))

def rec_total(query):
    tot = 1
    for cnt, bag in contents[query]:
        tot += cnt * rec_total(bag)
    return tot

print("part 2")
# subtract 1 bc of using tot = 1 as the base value
print(rec_total(query)-1)
