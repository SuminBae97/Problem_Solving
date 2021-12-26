import sys
n,m = map(int,sys.stdin.readline().split())
graph = [[0]*(m+1)]

for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    tmp = [0]+tmp
    graph.append(tmp)

for i in range(1,n+1):
    for j in range(1,m+1):
        graph[i][j] = max(graph[i][j-1],graph[i-1][j-1],graph[i-1][j]) + graph[i][j]


print(graph[n][m])
