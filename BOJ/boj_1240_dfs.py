import sys
sys.setrecursionlimit(10**5)

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(n-1):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dfs(start,end,dst):
    global visited
    visited[start]=True
    for val,weight in graph[start]:
        if visited[val]!=True:
            if val == end:
                global answer
                answer = dst+weight
                return

            dfs(val, end, dst + weight)


for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    visited = visited = [False]*(n+1)
    answer= 0
    dfs(s, e, 0)
    print(answer)

