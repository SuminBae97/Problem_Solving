from collections import Counter


def solution(participant, completion):
    p=Counter(participant)
    c=Counter(completion)
    answer=p-c 
    # hash의 counter collection module 응용방법
    return list(answer.keys())[0]
    
    
    