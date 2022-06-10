
input = [int(x) for x in open("input.txt", 'r')]

N = len(input)

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(i+2, N):
            if input[i] + input[j] + input[k] == 2020:
                print(input[i] * input[j] * input[k])
