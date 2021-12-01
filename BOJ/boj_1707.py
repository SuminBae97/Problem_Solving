#test_case = int(input())
import sys
from collections import deque
test_case = int(input())								
				
for _ in range(test_case):
	n,m = map(int,sys.stdin.readline().split())
	graph=[[] for _ in range(n+1)]
	color =[1]*(n+1)
	visited =[False]*(n+1)
	
	def bfs(i):
		q=deque([i])
		visited[i]=True	
		color[i]=1
		
		while q:
			v = q.popleft()
			for val in graph[v]:
				if visited[val]==False:
					q.append(val)
					color[val]= -color[v]
					visited[val]=True
	
	
	
	for _ in range(m):
		a,b = map(int,sys.stdin.readline().split())
		graph[a].append(b)
		graph[b].append(a)
		
	
		
	
	for i in range(1,n+1):
		if visited[i]==False:
			bfs(i)
	
	flg=False
	for val in range(1,n+1):
		c = color[val]
		for v in graph[val]:
			if c==color[v]:
				flg = True
			
	if flg:
		print("NO")
	else:
		print("YES")
					
	
	
