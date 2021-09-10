
#
# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]
#
# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]

lottos = [45,4,35,20,3,9]
win_nums = [20,9,3,45,4,35]
count = 0
prize = {6:1 , 5:2 , 4:3 , 3:4 , 2:5 , 1:6 ,0:6}
for i in range(len(win_nums)):
    for j in range(len(lottos)):
        if lottos[j] == win_nums[i]:
            count += 1
            lottos[j] = 9999
zero_val = lottos.count(0)

print(prize[count + zero_val],prize[count])