import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

indeg = [0]*(n+1)
indeg[0]=-1
direct =[[] for _ in range(n+1)]

q = deque()

for i in range(m):
	a,b = map(int,sys.stdin.readline().split())
	indeg[b]+=1
	direct[a].append(b)
	
for i in range(1,n+1):
	if indeg[i]==0:
		q.append(i)


while q:
	f = q.popleft()
	#direct[f]:3
	print(f,end=' ') 
	for d in direct[f]:
		indeg[d]-=1
		if indeg[d]==0:
			q.append(d)	
	
			
