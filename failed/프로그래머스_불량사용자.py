from itertools import permutations

def compare(str1,str2):
    if len(str1)!=len(str2):
        return False

    else:
        for i,j in zip(str1,str2):
            if j=="*":
                continue
            if i!=j:
                return False
        return True

def solution(user_id,banned_id):
    answer = []
    for options in permutations(user_id, len(banned_id)):

        ct = 0
        for usrid, banned in zip(options, banned_id):

            flag = compare(usrid, banned)
            if flag:
                ct += 1

        if ct == len(banned_id):
            if set(options) not in answer:
                answer.append(set(options))
    return len(answer)




