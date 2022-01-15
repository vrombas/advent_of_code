# the input here is a key mapping of the strings to their number value


def decode(seven_segments):
    display_key = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
    }

    len_5 = []
    len_6 = []

    for segment in seven_segments:
        if len(segment) == 2:
            display_key[1] = segment
        elif len(segment) == 3:
            display_key[7] = segment
        elif len(segment) == 4:
            display_key[4] = segment
        elif len(segment) == 5:
            len_5.append(segment)
        elif len(segment) == 6:
            len_6.append(segment)
        elif len(segment) == 7:
            display_key[8] = segment

    # decode [2, 3, 5]
    for segment in len_5:
        if set(display_key[7]).issubset(set(segment)):
            display_key[3] = segment
        else:
            if len(set(segment).intersection(set(display_key[4]))) == 3:
                display_key[5] = segment
            else:
                display_key[2] = segment

    # decode [0, 6, 9] len_6
    for segment in len_6:
        if set(display_key[4]).issubset(set(segment)):
            display_key[9] = segment
        else:
            if set(display_key[7]).issubset(set(segment)):
                display_key[0] = segment
            else:
                display_key[6] = segment

    return display_key


def unique_segments(input):
    digits_sum = 0
    for line in input:
        display_key = decode(line[0].split(" "))
        digit_string = ""

        for segments in line[1].split(" "):
            for k,v in display_key.items():
                if set(v) == set(segments):
                    digit_string += str(k)
        digits_sum += int(digit_string)

    return digits_sum


input = [x.strip("\n").split(" | ") for x in open("input.txt", 'r')]
# seven_segments = [x.strip("\n").split("|")[0].split(" ") for x in open("test.txt", 'r')]

print(unique_segments(input))
# print(decode(input[0]))
