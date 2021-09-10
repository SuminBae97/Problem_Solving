
#보류 진짜 모르겠음ㅁ....
from collections import deque
n,m = map(int,input().split())
graph=[]
visited=[]

for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    visited.append([False]*m)

dx =[1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue=deque()
    visited[x][y]=True
    queue.append((x,y))

    while queue:
        x_,y_ = queue.popleft()

        for i in range(4):
            nx = dx[i]+x_
            ny = dy[i]+y_

            if nx<0 or nx>=n or ny <0 or ny>=m:
                continue

            elif graph[nx][ny]==0 and visited[nx][ny]==False and graph[nx][ny]!=1:
                graph[nx][ny]=2
                visited[nx][ny]=True
                queue.append([nx,ny])


bfs(0,0)

print(graph)
print(visited)









