import sys
from collections import deque
graph =[]
m,n = map(int,sys.stdin.readline().split())

'''w = open("input.txt")
r = list(map(int,w.readline().split()))
while r:
	graph.append(r)
	r = list(map(int,w.readline().split()))
'''
for _ in range(m):
	graph.append(list(map(int,sys.stdin.readline().split())))
		

visited = [[False]*(n) for _ in range(m)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,mode):
	q = deque()
	visited[x][y]=True
	q.append((x,y))

	while q:
		x,y = q.popleft()
		cur_val = graph[x][y]
		
		for i in range(4):
			xp = x+dx[i]
			yp = y+dy[i]
			
			if xp<0 or xp>=m or yp<0 or yp>=n:
				continue
			
			if mode=='off':
				if graph[xp][yp]==0 and visited[xp][yp]!=True:
					q.append((xp,yp))
					visited[xp][yp]=True
					
			else:
				if graph[xp][yp]==1 and visited[xp][yp]!=True:
					q.append((xp,yp))
					visited[xp][yp]=True				
			
off_count=0

mode='off'					
for i in range(m):
	for j in range(n):
				if visited[i][j]!=True and graph[i][j]==0:
					bfs(i,j,mode)
					off_count+=1 			

visited = [[False]*(n) for _ in range(m)]

on_count=0
mode='on'					
for i in range(m):
	for j in range(n):
				if visited[i][j]!=True and graph[i][j]==1:
					bfs(i,j,mode)
					on_count+=1 		

print(off_count,on_count)
