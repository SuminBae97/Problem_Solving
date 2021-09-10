import sys
n = int(sys.stdin.readline())
seq = list(map(int,input().split()))
print(seq)
dp_1 = [1]*(1001)
dp_2 = [1]*(1001)

for i in range(n):
    for j in range(i):
        if seq[i]>seq[j]:
            dp_1[i] = max(dp_1[i],dp_1[j]+1)
print(dp_1[:n])
