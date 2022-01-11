import sys
n=19

graph = []

for _ in range(n):
	graph.append(list(map(int,sys.stdin.readline().split(" "))))

tcase = int(sys.stdin.readline())

for _ in range(tcase):
	x,y = map(int,sys.stdin.readline().split())
	
	x=x-1
	y=y-1
	
	for i in range(n):
		if graph[x][i]==1:
			graph[x][i]=0
		else:
			graph[x][i]=1
	
	for j in range(n):
		if graph[j][y]==1:
			graph[j][y]=0
		else:
			graph[j][y]=1
						
for i in range(19):
	for j in range(19):
		print(graph[i][j],end=' ')
	print()							
