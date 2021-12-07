import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

def bfs(x,y):
	q = deque()
	q.append((x,0))
	global n
	
	visited =[False]*(n+1)
	visited[x]=True
	
	while q:
		v, d = q.popleft()
		
		if v==y:
			return d
		
		for w,dist in graph[v]:
			if not visited[w]:
				visited[w]=True
				q.append((w,d+dist))
					
		

for _ in range(n-1):
	i,j,dist = map(int,sys.stdin.readline().split())
	graph[i].append((j,dist))
	graph[j].append((i,dist))
	




for _ in range(m):
	x,y = map(int,sys.stdin.readline().split())
	print(bfs(x,y))	
	
	
	




	

