import sys

n = int(sys.stdin.readline())
seq = list(map(int,sys.stdin.readline().split(" ")))

dp=[1]*(n+1)


for i in range(1,n):
	for j in range(i):
		if seq[j] < seq[i]:
			dp[i] = max(dp[j]+1,dp[i])
			
			
print(max(dp))
