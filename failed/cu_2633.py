import sys
n,k = map(int,sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))
# 5 4
# 1 3 5 7 9

left = 0
right = len(seq)-1

while left<=right:
    mid = (left+right)//2

    if seq[mid]<k:
        left = mid+1
    else:
        right = mid-1

print(left+1)