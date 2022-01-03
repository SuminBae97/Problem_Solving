import sys

n = int(sys.stdin.readline())
seq = list(map(int,sys.stdin.readline().split(" ")))

dp=[x for x in seq]
			

total_answer=[]
for i in range(1,n):
	answer=[]
	for j in range(i):
		if seq[j]<seq[i]:
			dp[i] = max(dp[j]+seq[i],dp[i])
			
print(max(dp))				
