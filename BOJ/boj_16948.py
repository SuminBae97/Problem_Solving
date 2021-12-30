import sys
from collections import deque

n=int(sys.stdin.readline())
visited = [[False]*n for _ in range(n)]
graph = [[0]*n for _ in range(n)]

coord =[
    [2,1],
    [2,-1],
    [0,-2],
    [0,2],
    [-2,-1],
    [-2,1]
]

r1,c1,r2,c2 = map(int,sys.stdin.readline().split())


def bfs(r1,c1):
    q=deque()
    visited[r1][c1]=True
    q.append((r1,c1))

    while q:
        xx,yy = q.popleft()
        for i in range(6):
            xp = xx+coord[i][0]
            yp = yy+coord[i][1]

            if xp<0 or xp>=n or yp<0 or yp>=n:
                continue

            elif visited[xp][yp]!=True:
                graph[xp][yp] = graph[xx][yy]+1
                visited[xp][yp]=True
                q.append((xp,yp))

bfs(r1,c1)

print(graph[r2][c2] if graph[r2][c2] else -1)



