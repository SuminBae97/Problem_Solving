import sys
from functools import reduce
from collections import deque,Counter
graph=[]
n = int(sys.stdin.readline())
visited = [[False]*n for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

a=[]











def bfs(x,y,cnt):
    q=deque()
    q.append([x,y])
    visited[x][y]=True
    graph[x][y]=cnt
    while q:
        _x,_y = q.popleft()
        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            elif graph[nx][ny]==1 and visited[nx][ny]==False:
                visited[nx][ny]=True
                graph[nx][ny]=cnt
                q.append([nx,ny])

cnt=0

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]==1:
            cnt+=1
            bfs(i,j,cnt)



print(cnt)
# 각 단지마다 집 개수 출력
# 2차원 배열을 1차원으로 쭈욱 펼치기
ans = reduce(lambda x,y : x+y, graph)
# 단지로 등록?된 집들만 ans 리스트에 남기기
ans = [x for x in ans if x > 0]
# cnt(단지번호) 별 개수(Counter.values()) 구하고 출력
ans = sorted(list(Counter(ans).values()))
print('\n'.join(map(str,ans)))