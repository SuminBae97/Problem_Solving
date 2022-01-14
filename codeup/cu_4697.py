import sys
from collections import deque

n = int(sys.stdin.readline())
#numvert = max(map(max, vertices))
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7

graph=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
max_height = max(map(max,graph))
if max_height==0:
    max_height=1


def bfs(x,y,max_height):
    q = deque()
    visited[x][y]=True
    q.append((x,y))

    while q:
        xp,yp = q.popleft()
        for i in range(4):
            nx = xp+dx[i]
            ny = yp+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            elif graph[nx][ny]>max_height and visited[nx][ny]==False:
                q.append((nx,ny))
                visited[nx][ny]=True

max_height_val = [i for i in range(0,max_height+1)]
answer=[]
for h in max_height_val:
    visited = [[False]*(n) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == False:
                bfs(i, j, h)
                count += 1
    answer.append(count)

print(max(answer))

