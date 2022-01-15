from aoc import read_file

list_lines = read_file("input.txt")

def intersects(list_lines):
    coordinates = {}
    num_intersects = 0
    for line in list_lines:
        inter = line.split("->")

        start_cord = inter[0].split(",")
        end_cord = inter[1].split(",")

        start_x = int(start_cord[0])
        start_y = int(start_cord[1])

        end_x = int(end_cord[0])
        end_y = int(end_cord[1])
        
        # horizontal
        if start_x != end_x and start_y == end_y:
            if (end_x, end_y) not in coordinates:
                coordinates[(end_x, end_y)] = 1
            else:
                coordinates[(end_x, end_y)] += 1

        while start_x != end_x and start_y == end_y:
            if (start_x, start_y) not in coordinates:
                coordinates[(start_x, start_y)] = 1
            else:
                coordinates[(start_x, start_y)] += 1
            # increment by +- 1
            start_x += (end_x - start_x)/abs(end_x - start_x)

        # vertical
        if start_y != end_y and start_x == end_x:
            if (end_x, end_y) not in coordinates:
                coordinates[(end_x, end_y)] = 1
            else:
                coordinates[(end_x, end_y)] += 1

        while start_y != end_y and start_x == end_x:
            if (start_x, start_y) not in coordinates:
                coordinates[(start_x, start_y)] = 1
            else:
                coordinates[(start_x, start_y)] += 1
            # increment by +- 1
            start_y += (end_y - start_y)/abs(end_y - start_y)

        # diagonal
        if start_y != end_y and start_x != end_x:
            if (end_x, end_y) not in coordinates:
                coordinates[(end_x, end_y)] = 1
            else:
                coordinates[(end_x, end_y)] += 1
        # guaranteed 45 degree diagonals
        while start_y != end_y and start_x != end_x:
            if (start_x, start_y) not in coordinates:
                coordinates[(start_x, start_y)] = 1
            else:
                coordinates[(start_x, start_y)] += 1
            # increment by +- 1
            start_y += (end_y - start_y)/abs(end_y - start_y)
            start_x += (end_x - start_x)/abs(end_x - start_x)

    for v in coordinates.values():
        if v > 1:
            num_intersects += 1
        
    return num_intersects


print(intersects(list_lines))
            








