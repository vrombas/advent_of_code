# Time: Total Time: 1hr 17min
# Part 1: 32min
# Part 2: 45min


def partTwo(input):
    opening = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    closing = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    scoring = { ")": 1, "]": 2, "}": 3, ">": 4 }
    scores = []

    for i, line in enumerate(input):
        corrupted = False
        stack = []
        for char in line:
            if char in closing:
                stack.append(char)
            elif stack.pop(len(stack) -1) != opening[char]:
                # print(f'line {i}: Expected {opening[char]}, but found {prev_char}')
                corrupted = True
                break

        if corrupted:
            continue

        compl_score = 0
        while len(stack) != 0:
            compl = closing[stack.pop(len(stack) -1)]
            compl_score = compl_score * 5 + scoring[compl]

        # print(f'line {i}: Score: {compl_score}, string: {compl}')
        scores.append(compl_score)

    scores.sort()
    return scores[len(scores)//2]


def partOne(input):
    opening = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }

    count = {}
    for i, line in enumerate(input):
        stack = []
        for char in line:
            if char not in opening:
                stack.append(char)
            elif stack.pop(len(stack) -1) != opening[char]:
                count[char] = count.get(char, 0) + 1
                # print(f'line {i}: Expected {opening[char]}, but found {prev_char}')
                break

    scoring = { ")": 3, "]": 57, "}": 1197, ">": 25137 }

    return sum(scoring[k] * c for (k, c) in count.items())


input = [x.rstrip("\n") for x in open("input.txt", "r")]

print(partOne(input))
print(partTwo(input))