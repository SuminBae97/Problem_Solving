def solution(arr1, arr2):
    answer = []
    for aval, bval in zip(arr1, arr2):
        l = []
        for av, bv in zip(aval, bval):
            val = av + bv
            l.append(val)

        answer.append(l)
    return answer
