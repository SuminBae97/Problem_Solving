import sys
n = int(input())

ans=[]

for _ in range(n):
	tmp = int(input())
	ans.append(tmp)
	
ans.sort()

for val in ans:
	print(val)
