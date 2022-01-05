n = int(input())

num = list(map(int, input().split()))
num_reverse = list(reversed(num))

dp = [1 for i in range(n)]
dp_r = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if num[i]> num[j]:
            dp[i] = max(dp[i],dp[j]+1)
        if num_reverse[i] > num_reverse[j]:
            dp_r[i] = max(dp_r[i],dp_r[j]+1)

answer = [0 for i in range(n)]
for i in range(n):
    answer[i] = dp[i] + dp_r[n-1-i]-1


print(max(answer))

