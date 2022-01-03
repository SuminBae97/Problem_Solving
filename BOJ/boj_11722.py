import sys

n = int(sys.stdin.readline())

seq  = list(map(int,sys.stdin.readline().split(" ")))

dp = [1]*(n)


for i in range(1,n):
	tmp=[]
	for j in range(i):
		if seq[i]<seq[j]:
			tmp.append(dp[j])
	
	if not tmp:
		continue
	
	else:
		dp[i]+=max(tmp)												
			
			
print(max(dp))
