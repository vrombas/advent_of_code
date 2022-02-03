import time


def growth_model(lan_fish, days):
    # Runs in O(n) time
    timer_list = [lan_fish.count(i) for i in range(9)]

    for day in range(0, days):
        num = timer_list.pop(0)  # get all lan_fish with day 0
        timer_list[6] += num
        timer_list.append(num)
        # print(timer_list)

    return sum(timer_list)






# Runs in O(n^2) time
    # while days > 0:
    #     new_fish = []
    #     for i, x in enumerate(lan_fish):
    #         lan_fish[i] -= 1  # decrement timer
    #         fish = int(lan_fish[i])
    #         if fish < 0:
    #             lan_fish[i] = 6
    #             new_fish.append(8)  # new fish
    #
    #     lan_fish += new_fish
    #     # print(lan_fish)
    #     days -= 1
    # return len(lan_fish)





t = 1
start = time.time()
while t > 0:
    x = open("input.txt")
    lan_fish = [int(x) for x in x.readline().split(",")]
    print(growth_model(lan_fish, 256))
    t -= 1
print("--- %s seconds ---" % (time.time() - start))
