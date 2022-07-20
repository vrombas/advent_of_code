part1 = 0
part2 = 0

for x in open("input.txt", 'r'):
    rang, letter, string = x.split(" ")
    
    l = int(rang.split("-")[0])
    r = int(rang.split("-")[1])

    letter = letter.rstrip(":")
    string.strip()

    if l <= string.count(letter) <= r:
        part1 += 1

    # going from 1-indexed to 0-indexed
    l -= 1
    r -= 1
    # only valid if exactly 1 location contains letter
    # only works when there are only 2 locations in question

    if (string[l] == letter) ^ (string[r] == letter):
        part2 += 1


print(part1)
print(part2)

