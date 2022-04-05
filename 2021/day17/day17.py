def solve():
    count = 0
    y_max = 0
    for dx in range(1000):
        for dy in range(-1000, 1000):
            count += simulate(dx, dy)
            # y_max = max(y_max, simulate(dx, dy))



    return count, y_max

def simulate(DX, DY):
    dx = DX
    dy = DY

    y_max = 0
    x = 0
    y = 0

    hit = False
    while x <= 129 and y >= -150:
    # while x <= 30 and y >= -10:
        y_max = max(y_max, y)
        # if 20<=x<=30 and -10<=y<=-5:
        if 81<=x<=129 and -150<=y<=-108:
            hit = True
            return 1
        x += dx
        y += dy

        dx -= sign(dx)
        dy -= 1

    if hit:
        return y_max

    return 0

def sign(x):
    return (int(x > 0) - int(x < 0))


print(solve())
# print(simulate(6, 9))
