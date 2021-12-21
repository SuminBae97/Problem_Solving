import sys
from collections import deque
tcase = int(sys.stdin.readline())


for _ in range(tcase):
	
	n = int(sys.stdin.readline())
	graph =[0] + list(map(int,sys.stdin.readline().split()))
	
	visited = [False]*(n+1)
	
	def bfs(x):
		q = deque([x])
		visited[x] = True
		
		while q:
			xp = q.popleft()
			
			next = graph[xp]
			
			if visited[next]!=True:
				visited[next]=True
				q.append(next)
				
	count = 0
	for i in range(1,n+1):
		if visited[i]==False:
			bfs(i)
			count+=1
	print(count)		
							
