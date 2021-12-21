import sys
sys.setrecursionlimit(10**6)

tcase = int(sys.stdin.readline())

for _ in range(tcase):
	n = int(sys.stdin.readline())
	visited = [False]*(n+1)
	graph = [0] + list(map(int,sys.stdin.readline().split()))

	def dfs(x):
		visited[x]=True
		next = graph[x]
		
		if visited[next]!=True:
			dfs(next)
		
	count = 0
	
	for i in range(1,n+1):
		if visited[i]!=True:
			dfs(i)
			count+=1
	
	print(count)					
