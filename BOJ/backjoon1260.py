

def bfs(v):
    visit[v]=1
    queue=[v]

    while queue:
        check=queue.pop(0)
        print(check,end=' ')

        for i in range(1,n+1):
            if s[check][i]==1 and visit[i]==0:
                visit[i]=1
                queue.append(i)

def dfs(v):

    visit[v]=1
    print(v,end=' ')
    for i in range(1,n+1):
        if visit[i]==0 and s[v][i]==1:
            dfs(i)

n,m, v = map(int, input().split())

s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1


dfs(v)
visit = [0 for i in range(n + 1)]
print()
bfs(v)