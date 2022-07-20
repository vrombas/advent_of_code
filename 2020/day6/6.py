from functools import reduce
x = open("input.txt", 'r').read()

answers = []
for s in x.split("\n\n"):
    answers.append(s.split("\n"))

# for each group, iterate through all 26 letters, 
# check each letter in each member's answers
# if it exists add 1 to cnt

alpha = "abcdefghijklmnopqrstuvwxyz"
cnt = 0
print(answers)
for grp in answers:
    for letter in alpha:
        good = True
        for surveys in grp:
            if letter not in surveys:
                good = False
                break
        if good:
            cnt += 1


print(cnt)

