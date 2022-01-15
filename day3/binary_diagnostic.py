from aoc import read_file

def gamma_epsilon(bin_values):
    gamma = ""  # add common bit
    epsilon = ""  # add uncommon bit

    for n in range(0, len(bin_values[0])):
        ones_count = sum([int(x[n]) == 1 for x in bin_values])
        gamma_val = 1 if ones_count > (len(bin_values)//2) else 0
        epsilon_val = 1 if gamma_val == 0 else 0

        gamma += str(gamma_val)
        epsilon += str(epsilon_val)

    print("dec Value of gamma:", int(gamma, 2))
    print("dec Value of epsilon:", int(epsilon, 2))
    print("multiplying two values:",  int(gamma, 2) * int(epsilon, 2))
    return

def life_support(bin_values):
    oxygen_bin = filter(bin_values, "oxygen")
    CO2_bin = filter(bin_values, "CO2")
    
    print("dec value of oxygen:", int(oxygen_bin, 2))
    print("dec value of CO2:", int(CO2_bin, 2))
    print("multipying two values:", int(oxygen_bin, 2) * int(CO2_bin, 2))
    
def filter(bin_values, flag):
    id = ''
    num_cols = len(bin_values[0])

    # This is a pretty disgusting for_loop, and I need to make it cleaner ->
    for n in range(0, num_cols):
        if (len(bin_values) == 1):
            break
        ones_count = sum([int(x[n]) == 1 for x in bin_values])
        if flag == "oxygen":
            id = "1" if ones_count > (len(bin_values)/2) else "0"
            if ones_count == len(bin_values)/2:
                id = '1'

        elif flag == "CO2":
            id = "0" if ones_count > (len(bin_values)/2) else "1"
            if ones_count == len(bin_values)/2:
                id = '0'

        temp = []
        for binVal in bin_values:
            if binVal[n] == id:
                temp.append(binVal)

        bin_values = temp
    return bin_values[0]


bin_values = read_file("binary_values.txt")
# bin_values = read_file("test.txt")
# Part 1
# gamma_epsilon(bin_values)

# Part 2
life_support(bin_values)


