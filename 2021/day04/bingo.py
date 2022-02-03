# I have stolen this solution from reddit user u/4HbQ for my own purposes ;)

import numpy as np

n, *b = open("test.txt", 'r')  # open n as head, *b as tail (split at "\n")

b = np.loadtxt(b, int).reshape(-1,5,5)     # load boards into 3D array

for n in map(int, n.split(',')):           # loop over drawn numbers
    b[b == n] = -1                         # mark current number as -1
    m = (b == -1)                          # get all marked numbers
    win = (m.all(1) | m.all(2)).any(1)     # check for win condition
    if win.any():
        print((b * ~m)[win].sum() * n)     # print winning score
        b = b[~win]                        # remove winning board


