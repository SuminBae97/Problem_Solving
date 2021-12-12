def solution(s):
    answer = True
    sum = 0
    for val in s:
        if val=="(":
            sum+=1
        elif val==")":
            sum-=1

        if sum<0:
            return False

    if sum==0:
        answer = True

    else:
        answer = False

    return answer

#print(solution("(()("))