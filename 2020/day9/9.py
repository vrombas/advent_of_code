input = [int(x) for x in open("input.txt", 'r')]
N = len(input)

def solve1(input, preamble):
    for i in range(preamble, N):
        good = False
        for j in range(i-preamble, i):
            for k in range(j+1, i+1):
#                 print(input[j], input[i], input[i])
                if (input[j] + input[k]) == input[i]:
                    good = True
        if not good:
            return input[i]

x = solve1(input, 25)
print(x)


for i in range(N):
    curr_tot = 0
    j = i
    while curr_tot < x:
        curr_tot += input[j]
        j += 1

    if curr_tot == x:
        rng = input[i:j]
        print(min(rng) + max(rng))
        break

