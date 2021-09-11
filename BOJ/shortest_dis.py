# 4 6
# 101111
# 101010
# 101011
# 111011
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
visited = [[False]*m for _ in range(n)]

for _ in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip()))
    graph.append(temp)
nx = [1,-1,0,0]
ny = [0,0,1,-1]


def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y]=True
    while q:
        x,y = q.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx<0 or dy<0 or dx>=n or dy>=m:
                continue
            elif visited[dx][dy]!=True and graph[dx][dy]!=0:
                q.append([dx,dy])
                graph[dx][dy] = graph[x][y]+1
                visited[dx][dy]=True

bfs(0,0)
print(graph[n-1][m-1])