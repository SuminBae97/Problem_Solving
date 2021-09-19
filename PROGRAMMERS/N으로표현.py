from collections import deque

def solution(N,number):
    answer=1
    count =1
    op = ["+","-","*","//","con"]
    q = deque([[N,count]])

    while True:
        vals,count = q.popleft()
        if vals==number:
            return count
        if count >8:
            return -1

        count+=1
        for i in op:
            if i=="+":
                val = vals+N
                q.append([val,count])
            elif i=="-":
                val = vals-N
                q.append([val, count])
            elif i=="*":
                val = vals*N
                q.append([val, count])
            elif i=="//":
                val = vals//N
                q.append([val, count])
            elif i=="con":
                a=  str(vals)+str(N)
                val = int(a)
                q.append([val, count])



print(solution(5,12))


