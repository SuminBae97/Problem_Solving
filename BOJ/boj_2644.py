import sys
from collections import deque
n  = int(sys.stdin.readline())
start,target = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

gp =[[] for _ in range(n+1)]

dist = [0]*(n+1)
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    gp[a].append(b)
    gp[b].append(a)


def bfs(start,target):
    q = deque([start])
    visited[start] = True

    while q:
        val = q.popleft()
        for nxt in gp[val]:
            if visited[nxt] == False:
                q.append(nxt)
                visited[nxt] = True
                dist[nxt] = dist[val] + 1

    if dist[target]==0:
        return -1
    else:
        return dist[target]

print(bfs(start,target))
