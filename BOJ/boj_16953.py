from collections import deque
import sys
start,target = map(int,sys.stdin.readline().split())
answer = -1
q = deque([(start,1)])

while q:
    i,cnt = q.popleft()

    if i==target:
        answer = cnt
        break

    if i*2 <=target:
        q.append([i*2,cnt+1])
    if int(str(i)+'1') <=target:
        q.append([int(str(i)+'1'),cnt+1])
print(answer)