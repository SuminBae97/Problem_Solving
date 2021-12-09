def solution(arr, divisor):
    answer = []
    
    for val in arr:
        if val%divisor==0:
            answer.append(val)
    
    if len(answer)==0:
        answer.append(-1)
    
    answer.sort()
    
    
    return answer
