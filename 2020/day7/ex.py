cnt = 0

def rec(timer):
    if timer == 0:
        return
    global cnt
    cnt += 1
    return rec(timer-1)

rec(6)
print(cnt)
