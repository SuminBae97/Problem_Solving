import sys
from collections import deque
n,m =map(int,sys.stdin.readline().split())
MAX = 200001

visited = [False]*MAX
dst = [0]*(MAX)

def bfs(n,m):
    q = deque()
    q.append(n)
    visited[n]=True

    while q:
        v = q.popleft()
        if v==m:
            break

        for val in [v+1,v-1,2*v]:
            if val < 0 or val >=MAX:
                continue

            elif visited[val]==False:
                visited[val] =True
                dst[val] = dst[v]+1
                q.append(val)
bfs(n,m)
print(dst[m])


