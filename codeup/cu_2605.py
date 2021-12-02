# 2 1 5 1 1 3 4
# 2 1 5 1 3 5 3
# 2 3 4 5 2 2 4
# 4 4 3 2 3 1 3
# 4 3 5 3 1 4 3
# 5 4 4 3 3 5 5
# 2 1 3 5 1 1 2
#빨강 = 1 , 노랑 = 2 , 파랑 = 3 , 초록 = 4 , 보라 = 5
import sys
from collections import deque

graph=[]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


for _ in range(7):
    tmp = list(map(int,sys.stdin.readline().split()))
    graph.append(tmp)

def bfs(x,y,val):
    q = deque([(x,y)])
    visited[x][y]=True
    count=1

    while q:
        x_,y_ = q.popleft()
        for i in range(4):
            xp = x_+dx[i]
            yp = y_+dy[i]

            if xp<0 or xp>=7 or yp<0 or yp>=7:
                continue
            elif visited[xp][yp] == False and graph[xp][yp]==val:
                visited[xp][yp]=True
                q.append([xp,yp])
                count+=1
    return count


ct=0

for k in range(1,6):
    visited = [[False] * 7 for _ in range(7)]
    for i in range(7):
        for j in range(7):
            if not visited[i][j] and graph[i][j] == k:
                m = bfs(i, j, k)
                if m < 3:
                    continue
                else:
                    ct += 1


print(ct)









