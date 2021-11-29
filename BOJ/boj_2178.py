import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())


graph=[]

for _ in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip()))
    graph.append(temp)

visited = [[False]*m for _ in range(n)]

dx = [1,-1, 0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q=deque([(x,y)])
    visited[x][y]=True

    while q:
        x_,y_ = q.popleft()
        for i in range(4):
            xp = dx[i]+x_
            yp = dy[i]+y_

            if xp<0 or xp>=n or yp<0 or yp>=m:
                continue

            elif graph[xp][yp]!=0 and visited[xp][yp]!=True:
                q.append([xp,yp])
                visited[xp][yp]=True
                graph[xp][yp] = graph[x_][y_]+1

bfs(0,0)

print(graph[n-1][m-1])