# Time: Total Time: 1hr 17min
# Part 1: 32min
# Part 2: 45min


def partTwo(input):
    pairing = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    reverse_pairing = {
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
            if char in pairing.keys():
                prev_char = stack.pop(len(stack) - 1)
                if prev_char != pairing[char]:
                    # print(f'line {i}: Expected {pairing[char]}, but found {prev_char}')
                    corrupted = True
                    break
            else:
                stack.append(char)
        if corrupted:
            continue

        compl = ""
        while len(stack) != 0:
            compl += reverse_pairing[stack.pop(len(stack) -1)]

        compl_score = 0
        for char in compl:
            compl_score *= 5
            compl_score += scoring[char]
        # print(f'line {i}: Score: {compl_score}, string: {compl}')
        scores.append(compl_score)

    scores.sort()
    return scores[len(scores)//2]


def partOne(input):
    pairing = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }

    count = {}
    for i, line in enumerate(input):
        stack = []
        for char in line:
            if char in pairing.keys():
                prev_char = stack.pop(len(stack) - 1)
                if prev_char != pairing[char]:
                    count[char] = count.get(char, 0) + 1
                    # print(f'line {i}: Expected {pairing[char]}, but found {prev_char}')
                    # input.pop(i) will not work (skips next line when popped)
                    break
            else:
                stack.append(char)

    scoring = { ")": 3, "]": 57, "}": 1197, ">": 25137 }

    return sum(scoring[k] * c for (k, c) in count.items())


input = [x.rstrip("\n") for x in open("input.txt", "r")]

print(partOne(input))
print(partTwo(input))