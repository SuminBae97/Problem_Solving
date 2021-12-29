import sys
n,m = map(int,sys.stdin.readline().split())

val =[0]
weight =[0]

for i in range(n):
	it,vals = map(int,sys.stdin.readline().split())
	weight.append(it)
	val.append(vals)


dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
	for j in range(1,m+1):
		
		if weight[i] <= j:
			dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+val[i])
		else:
			dp[i][j] = dp[i-1][j]


print(dp[n][m])			
