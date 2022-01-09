import sys
from collections import deque
from pprint import pprint

graph = []
visited = [[False] * (10) for _ in range(10)]
for i in range(10):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    graph.append(tmp)


def bfs(x, y):
    graph[x][y] = 9
    visited[x][y] = True
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        if x<0 or x>=9 or y<0 or y>=9:
            continue

        if graph[x][y]==2:
            graph[x][y]=9
            return

        elif graph[x][y+1]==1:
            if x+1==9:
                continue

            q.append((x+1,y))

            if graph[x+1][y]==2:
                graph[x+1][y]=9
                return
            else:
                graph[x+1][y]=9


        else:
            if y+1==9:
                continue
            q.append((x,y+1))
            if graph[x][y+1]==2:
                graph[x][y+1]=9
                return
            else:
                graph[x][y+1]=9

bfs(1,1)
for i in range(10):
    for j in range(10):
        print(graph[i][j],end=" ")
    print()