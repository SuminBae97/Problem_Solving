import sys
from collections import deque

#tcase = int(sys.stdin.readline())
for _ in range(tcase):
	n = int(sys.stdin.readline())
	graph = [0] + list(map(int,sys.stdin.readline().split()))

	visited = [False]*(n+1)
	is_cycle = [False]*(n+1)


	def bfs(x):
		q = deque([x])
		visited[x]=True
		check_q =[]	
		while q:
			xp = q.popleft()
			next = graph[xp]
			if x==next:
				is_cycle[x]=True
				for val in check_q:
					is_cycle[val]=True
			
			if visited[next]!=True:
				q.append(next)
				check_q.append(next)
				visited[next]=True
						
	for i in range(1,n+1):
		if is_cycle[i]!=True or visited[i]!=True:
			bfs(i)
			
	print(is_cycle[1:].count(False))		
					
