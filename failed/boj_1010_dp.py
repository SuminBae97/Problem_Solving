import sys
tcase = int(sys.stdin.readline())
for _ in range(tcase):
    n, m = map(int, sys.stdin.readline().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1:
                dp[i][j] = j
            elif i == j:
                dp[i][j] = 1
            else:
                if j > i:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    print(dp[n][m])