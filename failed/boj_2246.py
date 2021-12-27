import sys
n,k = map(int,sys.stdin.readline().split())
coin= []
for _ in range(n):
	tmp = int(sys.stdin.readline())
	coin.append(tmp)
	
dp = [0]*(k+1)
dp[0]=1
 
for i in coin:
	for j in range(1,k+1):
		if j-i>=0:
			dp[j] = dp[j]+dp[j-i]
			
print(dp[k])			
