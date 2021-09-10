import sys
#↑, ↖, ←, ↙, ↓, ↘, →, ↗
#0, 1, 2, 3, 4, 5, 6, 7

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

a = [[] for _ in range(4)]
fish = [[] for _ in range(16)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        a[i].append([temp[j]-1, temp[j+1]-1])
        fish[temp[j]-1] = [i, j // 2]
print(fish)
print(a)

def fish_rotate(x,y):
    pass