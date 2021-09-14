import sys
n= int(sys.stdin.readline())


def solution(n):
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,n+1):

        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]



for i in range(n):
    val = int(sys.stdin.readline())
    print(solution(val))
import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):

    val = int(sys.stdin.readline())

    dp = [0] * (12)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[val])

# 9/14 review 1
