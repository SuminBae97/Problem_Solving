from collections import deque
def solution(numbers, target):
    answer = 0
    leaves = [0]
    answer = []
    for num in numbers:
        temp = []
        for val in leaves:
            temp.append(val + num)
            temp.append(val - num)
        leaves = temp

    return leaves.count(target)

#print(solution(numbers,target))