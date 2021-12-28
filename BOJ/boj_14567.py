import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

indeg = [0]*(n+1)
graph = [[] for _ in range(n+1)]
answer = [1]*(n+1)
for _ in range(m):
	a,b =map(int,sys.stdin.readline().split())
	graph[a].append(b)
	indeg[b]+=1


q = deque()

for i in range(1,n+1):
	if indeg[i]==0:
		answer[i]=1
		q.append(i)

while q:
	val = q.popleft()
		
	for d in graph[val]:
		indeg[d]-=1
		if indeg[d]==0:
			answer[d]+=answer[val]
			q.append(d)

for i in range(1,n+1):
	print(answer[i],end=" ")		
			
			
		
	
