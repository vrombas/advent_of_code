def main():
    def rec(timer, cnt):
        if timer == 0:
            return cnt
        return rec(timer-1, cnt+1)

    print(rec(6, 0))


main()
