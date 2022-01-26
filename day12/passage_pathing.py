from collections import defaultdict, Counter, deque

# Time: 45 min, Unsolved


def partOne(input):
    neighbors = defaultdict(list)
    ans = 0

    for edge in input:
        neighbors[edge[0]].append(edge[1])
        neighbors[edge[1]].append(edge[0])

    start = ("start", {"start"}, ["start"], None)

    Q = deque([start])  # has to be in [] otherwise each char is added individually

    # run BFS to find paths containing end
    while Q:
        node, visited, path, twice = Q.popleft()
        for neighbor in neighbors[node]:
            if neighbor == "end":
                print(path + ["end"])
                ans += 1
                continue

            if neighbor not in visited:
                new_visited = set(visited)
                if neighbor.islower():
                    new_visited.add(neighbor)
                Q.append((neighbor, new_visited, path + [neighbor], twice))

            elif neighbor not in ["start", "end"] and twice is None:
                Q.append((neighbor, visited, path + [neighbor], neighbor))

    # when appending to Q, make sure that you don't change the values of the current node
    # only change values when adding new objects to Q

    return ans


def partTwo(input):
    return None


input = [x.rstrip("\n").split("-") for x in open("input.txt", 'r')]
print(partOne(input))
