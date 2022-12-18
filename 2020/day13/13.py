f = open("input.txt", 'r')

N = int(f.readline())
input = f.readline().split(",")

def solve1(N, input):
    times = [int(x) for x in input if x != 'x']

    for i in range(N, N+50):
        for t in times:
            if i%t == 0:
                print(i, t)
                return (i-N)*t


print(solve1(N, input))
