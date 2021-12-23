import sys

sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline


def dfs(x):
   global ans
   visited[x]=True
   cycle.append(x)
   next_node = graph[x]
   
   if visited[next_node]==False:
   	dfs(next_node)
   	
   else:
   	if next_node in cycle:
   		ans +=cycle[cycle.index(next_node):]
   	return	
   

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if not vis[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))
