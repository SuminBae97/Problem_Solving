import sys
from collections import deque

dx =[1,-1,0,0]
dy = [0,0,1,-1]

r,c = map(int,sys.stdin.readline().split())
visited = [[False]*c for _ in range(r)]
graph=[]

for _ in range(r):
    tmp = list(sys.stdin.readline().rstrip())
    graph.append(tmp)

def bfs(x,y):
    global l_c
    global w_c

    q = deque()
    visited[x][y] = True
    q.append((x,y))



    while q:
        xx,yy = q.popleft()

        if graph[xx][yy] == "v":
            w_c += 1
        elif graph[xx][yy] == "o":
            l_c += 1

        for i in range(4):
            xp = xx+dx[i]
            yp = yy+dy[i]

            if xp<0 or xp>=r or yp<0 or yp>=c:
                continue

            elif visited[xp][yp]!=True and graph[xp][yp]!="#":
                visited[xp][yp]=True
                q.append((xp,yp))

wolf_count=0
lamb_count=0

for i in range(r):
    for j in range(c):
        if graph[i][j]!="#" and visited[i][j]==False:
            w_c=0
            l_c=0
            bfs(i,j)

            if w_c>=l_c:
                l_c = 0
            else:
                w_c=0

            wolf_count+=w_c
            lamb_count+=l_c


print(lamb_count,wolf_count)
