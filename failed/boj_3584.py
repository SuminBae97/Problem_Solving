import sys
t = int(sys.stdin.readline())

for _ in range(t):
	n= int(sys.stdin.readline())
	parents =[0 for _ in range(n+1)]

	for i in range(n-1):
		a,b = map(int,sys.stdin.readline().split())
		parents[b]=a
	

	a,b = map(int,sys.stdin.readline().split())
	a_parents=[a]
	b_parents=[b]
	while parents[a]:
		a_parents.append(parents[a])
		a=parents[a]
	
	while parents[b]:
		b_parents.append(parents[b])
		b = parents[b]
	
	a_root = len(a_parents)-1
	b_root = len(b_parents)-1
	
	while a_parents[a_root]==b_parents[b_root]:
		a_root-=1
		b_root-=1
		
	print(a_parents[a_root+1])	
	
	
	
	

