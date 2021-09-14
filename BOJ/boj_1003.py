import sys
dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1

for i in range(2,len(dp)):
    for j in range(len(dp[i])):
        dp[i][j] = dp[i-1][j]+dp[i-2][j]

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n = int(sys.stdin.readline())
    print(dp[n][0] ,dp[n][1])

#풀이법
# 각 정수마다 f(0)이 호출된 횟수와 f(1)이 호출된 횟수는
# 피보나치의 원리와 동일하게 적용이 된다.
# 그렇기 때문에 자료구조를 우선 0이 호출된 횟수와 1이 호출된 횟수를 저장하기 위한
# 이차원 리스트로 지정을 하고
# 각 정수별로 이전 2개의 0으 값과 1의 값을 각각 더해주면 된다.