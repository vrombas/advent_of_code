from aoc import read_planned_course
instructions = read_planned_course("planned_course.txt")

def navigate(directions):
    aim, depth, pos = 0, 0, 0

    for d in directions:
        direction = d[0]
        magnitude = int(d[1])
        
        if (direction == "forward"):
            pos += magnitude
            depth += (aim * magnitude)

        if (direction == "up"):
            # depth -= magnitude
            aim -= magnitude

        if (direction == "down"):
            # depth += magnitude
            aim += magnitude

    print("Depth:", depth)
    print("Position:", pos)
    print("Depth*Position:", depth * pos)


navigate(instructions)


