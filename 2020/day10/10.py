input = [int(x) for x in open("test.txt", 'r')]

input.append(0)
input.sort()    

input.append(input[len(input)-1] + 3)



N = len(input)
diff1 = 0
diff3 = 0

for i in range(N-1):
    if input[i+1] - input[i] == 1:
        diff1 += 1
    elif input[i+1] - input[i] == 3:
        diff3 += 1
    else:
        print('err')

# edge cases of 0 and N
print(diff1, diff3, diff1 * diff3)


# apparently part 2 requires dynamic programming

unneeded = 0
i = 0
while i < N:
    thres = input[i] + 3
    # given that the numbers are distinct, only search up to next 3 spaces
    good = False
    j = 1
    while j < 4:
        if input[i+j] == thres:
            good = True
            break
        j+= 1
    if good:
        unneeded += 
    assert(idx != 0)
    if idx == -1:
        i += 1
        continue

    unneeded += idx
    i += idx

