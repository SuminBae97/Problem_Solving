import sys
h,w = map(int,sys.stdin.readline().split())

graph = [[0]*(w) for _ in range(h)]

num = int(sys.stdin.readline())

for _ in range(num):
	length, direct , x,y = map(int,sys.stdin.readline().split(" "))
	graph[x-1][y-1]=1
	
	if direct==0:
		for i in range(length):
			graph[x-1][y+i-1]=1
	elif direct==1:
		for i in range(length):
			graph[x-1+i][y-1]=1

for i in range(h):
	for j in range(w):
		print(graph[i][j], end=' ')
	print()	
	
					
					
			
