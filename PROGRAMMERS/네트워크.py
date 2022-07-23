a=[
	[1,1,0],
	[1,1,0],
	[0,0,1]
	]
a=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

from collections import deque    

def bfs(start,graph,visited):
#     graph =[[] for _ in range(n)]
#     for i in range(len(computers)):
#         for j in range(len(computers[i])):
#             if i==j:
#                 continue
#             elif a[i][j]==1:
#                 graph[i].append(j)
    
#     visited = [False]*(n)
#     count = 0
#     visited=[start]=True
    q = deque()
    q.append(start)
    while q:
        val = q.popleft()
        for nxt in graph[val]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt]
        
    

def solution(n, computers):
    graph =[[] for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i==j:
                continue
            elif computers[i][j]==1:
                graph[i].append(j)
    
    visited = [False]*(n)
    count = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i,graph,visited)
            count+=1
    print(count)
    
    
solution(3,a)
