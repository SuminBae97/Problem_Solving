import math



def solution(n):
    s = [True]*(n+1)
    m= int((n+1)**0.5)
    for i in range(2,m+1):
        if s[i]==True:
            for j in range(i+i,n+1,i):
                s[j]=False

    return len([i for i in range(2,n+1) if s[i]==True])


print(solution(10))
