from collections import deque
import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dst = [0]*(n+1)
for _ in range(n):
    info = list(map(int,sys.stdin.readline().split()))
    root = info[0]
    for i in range(1,len(info)-2,2):
        node = info[i]
        weight = info[i+1]
        tree[root].append([node,weight])

# n = int(sys.stdin.readline())
# tree = [[] for _ in range(n + 1)]
# visited = [False]*(n+1)
# dst = [0]*(n+1)
#
#
# for _ in range(n):
#     c = list(map(int, sys.stdin.readline().split()))
#     for e in range(1, len(c) - 2, 2):
#         tree[c[0]].append((c[e], c[e + 1]))

def bfs(start):
    q = deque()
    q.append(start)
    visited[start]=True

    while q:
        val = q.popleft()
        for node_info in tree[val]:
            node = node_info[0]
            weight = node_info[1]

            if visited[node]!=True:
                dst[node] = dst[val]+weight
                visited[node]=True
                q.append(node)
bfs(2)
max_index = dst.index(max(dst))
visited = [False]*(n+1)
bfs(max_index)
max_index2 = dst.index(max(dst))
print(dst[max_index2] - dst[max_index])





