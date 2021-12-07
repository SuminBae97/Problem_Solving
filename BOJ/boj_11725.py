import sys 
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

parent = [0]*(n+1)


for _ in range(n-1):
	a,b = map(int,sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)
	

def bfs(x):
	visited[x]=True
	q = deque([x])
	
	while q:
		xp = q.popleft()
		
		
		for val in graph[xp]:
			if visited[val]!=True:
				visited[val]=True
				parent[val] = xp
				q.append(val)

bfs(1)				
			
for i in range(2,len(parent)):
	print(parent[i])		
	
	
	
