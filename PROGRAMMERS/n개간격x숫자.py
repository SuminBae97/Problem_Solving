def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        nx = x * i
        answer.append(nx)

    return answer