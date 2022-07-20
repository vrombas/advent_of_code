import re

data = open("test.txt", 'r').read()

for pp in data.split("\n\n"):
    d = {}
    pp.replace(" ", "\n")
    for kv in pp.split(" "):
        print(kv)
        k,v = kv.split(":")
        d[k] = v
    print(d)


