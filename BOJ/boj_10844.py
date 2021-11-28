from pprint import pprint
n = int(input())

dp = [[0]*(101) for _ in range(10)]

for i in range(1,10):
    dp[i][1]=1

for j in range(2,n+1):
    for k in range(0,10):
        if k==0:
            dp[k][j] = dp[k+1][j-1]
        elif k==9:
            dp[k][j] = dp[k-1][j-1]
        else:
            dp[k][j] = dp[k+1][j-1] + dp[k-1][j-1]
sum = 0
for a in range(10):
    sum+=dp[a][n]
print(sum%(10**9))



