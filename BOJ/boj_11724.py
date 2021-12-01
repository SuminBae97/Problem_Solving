import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
	a,b = map(int,sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)


def bfs(i):
	q=deque([i])
	visited[i]=True
	
	while q:
		val = q.popleft()
		for v in graph[val]:
			if visited[v]==False:
				q.append(v)
				visited[v]=True
		
count=0	
for i in range(1,n+1):
	if visited[i]==False:
		bfs(i)
		count+=1
print(count)

