import sys
#a=[(1,2),(0,10)]

#c = sorted(a,key=lambda x:x[1])
#b = {"apple":0,"banna":30}
#d= sorted(b.items(),key = lambda x:x[1],reverse=True)


n = int(input())
ans=[]

for _ in range(n):
	a,b = map(int,sys.stdin.readline().split())
	ans.append((a,b))

ans = sorted(ans,key=lambda x:(x[1],x[0]))

for val in ans:
	print(val[0],val[1]) 	
