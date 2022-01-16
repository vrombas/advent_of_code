def count_increases(data):
    return sum(data[i] > data[i - 1] for i in range(1, len(data)))


def count_window_increases(data, window):
    # (a, b, c) > (b, c, d) only if d > a
    # (therefore no need to sum, just check 0th and last indexes)
    return sum(data[i] > data[i - window] for i in range(window, len(data)))


sonar_data = [int(x) for x in open('/sonar_data.txt')]

print("Part 1: " + str(count_increases(sonar_data)))
print("Part 2: " + str(count_window_increases(sonar_data, 3)))
