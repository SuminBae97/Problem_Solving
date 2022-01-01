import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for i in range(n + 1)]
distance = [0]*(n+1)

for i in range(1, n):
    p, c, w = map(int, input().split())
    graph[p].append([c, w])
    graph[c].append([p, w])

def bfs(start):
    visited = [False]*(n+1)
    visited[start]=True
    q = deque([start])

    while q:
        val = q.popleft()
        for vv in graph[val]:
            node = vv[0]
            weight = vv[1]

            if visited[node]!=True:
                distance[node] = distance[val]+weight
                visited[node]=True
                q.append(node)


bfs(1)
max_node = distance.index(max(distance))
bfs(max_node)
second_max_node = distance.index(max(distance))

print(distance[second_max_node] - distance[max_node ])







