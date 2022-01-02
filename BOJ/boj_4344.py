import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    tmp = list(map(int, sys.stdin.readline().split()))
    s_num = tmp[0]
    score = tmp[1:]
    avg_score = sum(score)/s_num
    ct = 0
    for student in score:
        if student > avg_score:
            ct += 1

    rate = (ct / s_num) * 100
    print(f'{rate:.3f}%')




