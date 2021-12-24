import sys
sys.setrecursionlimit(10**6)

test_case = int(sys.stdin.readline())

for _ in range(test_case):
	n = int(sys.stdin.readline())
	visited =[False]*(n+1)
	graph =[0] + list(map(int,sys.stdin.readline().split()))
	answer =[]
	
	def dfs(x):
		visited[x]=True
		global answer
		cycle.append(x)
		next = graph[x]

		if visited[next]==True:
			if next in cycle:
				answer+=(cycle[cycle.index(next):])
			return 
		
		else:
			dfs(next)
					
	for i in range(1,n+1):
		if not visited[i]:
			cycle=[]
			dfs(i)
	print(n-len(answer))
			
			
	
	
	
