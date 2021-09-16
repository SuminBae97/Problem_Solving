
n,k = map(int, input().split())
bag = [[0,0]]
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
    bag.append(list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = bag[i][0]
        val  = bag[i][1]

        if j<weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight]+val , dp[i-1][j])


print(dp[n][k])

