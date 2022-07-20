
input = [int(x) for x in open("input.txt", 'r')]


def day1(input):
    N = len(input)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i != j != k:
                    if input[i] + input[j] + input[k] == 2020:
                        return input[i] * input[j] * input[k]

print(day1(input))
