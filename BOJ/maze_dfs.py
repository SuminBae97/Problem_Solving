import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())
graph =[]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))


def dfs(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx>=n or nx<0 or ny<0 or ny>=m:
            continue
        elif graph[nx][ny]==1:
            graph[nx][ny] = graph[x][y]+1
            dfs(nx,ny)

    return graph[n-1][m-1]
dfs(0,0)
print(graph[n-1][m-1])

