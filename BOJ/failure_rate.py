def solution(N, stages):
    answer = []
    fail_rate = []

    for i in range(N):
        stage_num = i + 1
        count = 0
        for val in stages:
            if val >= stage_num:
                count += 1

        rate = stages.count(stage_num) / count
        fail_rate.insert(i, rate)


    while sum(fail_rate)!= -N:
        for index, rate in enumerate(fail_rate):
            max_rate = max(fail_rate)

            if max_rate == rate:
                answer.append(index + 1)

                fail_rate[index] = -1

    return answer

