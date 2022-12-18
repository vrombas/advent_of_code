instructs = [x.strip() for x in open("test.txt", 'r')]
N = len(instructs)


for i in range(N):
    cmd, num = instructs[i].split(" ")
    if cmd == "nop":
        instructs[i] = "jmp " + num
    elif cmd == "jmp":
        instructs[i] = "nop " + num
    else:
        continue
    for x in instructs:
        print(x)
    seen = set()
    head = 0
    acc = 0

    t = 0
    while head < N and t < 1000:
        t += 1
        if head in seen:
            break

        seen.add(head)
        cmd, num = instructs[head].split(" ")

        if cmd == "nop":
            head += 1

        elif cmd == "acc":
            head += 1
            acc += int(num)

        elif cmd == "jmp":
            head += int(num)

        else:
            assert False

        if head == N:
            print(acc)


