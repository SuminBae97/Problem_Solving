import sys
from collections import deque
dist = [0]*1000001
visited = [False]*(1000001)

n = int(input())

def bfs(n):
	q = deque([n])
	visited[n]=True
	
	while q:
		val= q.popleft()
		
		if val%3==0 and visited[val//3]==False:
			tmp = val//3
			q.append(tmp)
			visited[tmp] = True
			dist[tmp] = dist[val]+1
			
	
		if val%2==0 and visited[val//2]==False:
			tmp = val//2
			q.append(tmp)
			visited[tmp]=True
			dist[tmp] = dist[val]+1
		
		if visited[val-1]==False:
			tmp = val-1
			if tmp==0:
				break
			q.append(tmp)
			visited[tmp]= True
			dist[tmp] = dist[val]+1
		
		
	return dist[1]

print(bfs(n))
																
			


