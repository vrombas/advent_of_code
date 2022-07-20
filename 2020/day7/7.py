from collections import defaultdict
parents = defaultdict(list)
bag_cnt = defaultdict(int)


for l in open("input.txt"):
    line = l.strip()
    parent, children = line.split(" contain ")
    parent = parent.rstrip("s")

    for b in children.strip(".\n").split(","):
        bag = b.strip()  # idk how to avoid this
        if bag == "no other bags":
            continue

        num = int(bag[:bag.find(" ")].strip())
        bag_id = bag[bag.find(" "):].strip().rstrip("s")
        bag_cnt[parent] += num

        parents[bag_id].append(parent)

for x in parents.items():
    pass

# complete>

query = "shiny gold bag"
visited = set()
# visited = set([query])
Q = [query]
while Q:
    child = Q.pop()
    for p in parents[child]:
        if p not in visited:
            Q.append(p)
        visited.add(p)


# part 1
print(len(visited))
# TODO
# part 2

assert False 
# TODO 
# recursive function there to check all parent bags and add to cnt
def rec_search(bag, visited):
    ps = parents.get(bag, [])
    for p in ps:
        visited.add(p)
    print(visited)
    for p in ps:
        visited = rec_search(p, visited)
    return visited

print(len(rec_search("shiny gold bag", set())))
