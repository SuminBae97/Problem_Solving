import sys 
from pprint import pprint
from collections import deque, Counter
from functools import reduce

n = int(input())
graph=[]
visited = [[False]*n for _ in range(n)]




dx=[1,-1,0,0]
dy=[0,0,1,-1]



for _ in range(n):
	tmp = list(map(int,sys.stdin.readline().rstrip()))
	graph.append(tmp)
	
	
count=1
bfs_count=0

def bfs(x,y,count):
	q=deque([(x,y)])
	visited[x][y]=True
	graph[x][y]=count
	apart_count=1
	
	
	while q:
		x_,y_ = q.popleft()
		for i in range(4):
			xp = x_+dx[i]
			yp = y_+dy[i]
			
			if xp<0 or xp>=n or yp<0 or yp>=n:
				continue
				
			elif graph[xp][yp]==1 and visited[xp][yp]==False:
				visited[xp][yp]=True
				q.append([xp,yp])
				graph[xp][yp]=count
				apart_count+=1
				
	return apart_count

result=[]
for i in range(n):
	for j in range(n):
		if visited[i][j]==False and graph[i][j]==1:
			ac = bfs(i,j,count)
			result.append(ac)
			bfs_count+=1
			count+=1

						
print(bfs_count)
ans = reduce(lambda x,y : x+y, graph)
# 단지로 등록?된 집들만 ans 리스트에 남기기
ans = [x for x in ans if x > 0]
# cnt(단지번호) 별 개수(Counter.values()) 구하고 출력
ans = sorted(list(Counter(ans).values()))
print('\n'.join(map(str,ans)))

