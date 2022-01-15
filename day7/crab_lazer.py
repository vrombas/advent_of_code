import time


def crab_alignment(x_pos):
    count = {}
    # average of modes
    for x in x_pos:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1

    mode_list = []
    mode = max(count.values())

    for k, v in count.items():
        if v == mode:
            mode_list.append(k)

    optimal_x = sum(mode_list) / len(mode_list)

    return sum([abs(x-optimal_x) for x in x_pos])

def test(x_pos):
    upper_bound = max(x_pos)
    lower_bound = min(x_pos)

    buffer_lst = []

    for a in range(lower_bound, upper_bound):
        # constant rate fuel consumption
        # buffer_lst.append(sum([abs(x-a) for x in x_pos]))

        # increasing rate (x2 = (x1)(x1 + 1)/2)
        buffer_lst.append(sum([abs(x-a)*(abs(x-a)+1)/2 for x in x_pos]))

    max_value = min(buffer_lst)
    print("x value: ", buffer_lst.index(max_value))
    return max_value





f = open("input.txt", 'r')
x_pos = [int(x) for x in f.readline().strip().split(',')]

start = time.time()
print("fuel: ", test(x_pos))
print("Runtime: %1.4ss" % (time.time() - start))
# print(crab_alignment(x_pos))
