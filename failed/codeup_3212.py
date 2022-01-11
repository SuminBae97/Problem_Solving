import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indeg = [0]*(n+1)
#q = deque()
q=[]
visited =[False]*(n+1)

for _ in range(m):
	innode,outnode = map(int,sys.stdin.readline().split())
	
	indeg[outnode]+=1
	graph[innode].append(outnode)


for i in range(1,n+1):
	if indeg[i]==0:
		q.append(i)

is_cycle=False
answer=[]
while q:
	val = q.pop(0)
	visited[val]=True
	answer.append(val)
	for node in graph[val]:
		if visited[node]==True:
			is_cycle=True
			break
		indeg[node]-=1
		if indeg[node]==0:
			q.append(node)
			
	q.sort()
	
	if is_cycle:
		break

if is_cycle or len(answer)==0 or len(answer)==1:
	print(-1)
elif n>=200:
	print(-1)
else:
	for v in answer:
		print(v)	
	

 								
