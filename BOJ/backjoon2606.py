
def bfs(v):
    visit[v]=1
    queue=[v]

    while queue:
        next=queue.pop(0)

        for i in range(1,n+1):
            if visit[i]==0 and graph[next][i]==1:
                queue.append(i)
                visit[i]=1

def check(visit):
    count=0
    for i in range(len(visit)):
        if visit[i]==1:
            count+=1

    return count-1




n=int(input())
m=int(input())

visit=[0 for i in range(n+1)]
graph=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())

    graph[x][y]=1
    graph[y][x]=1


bfs(1)
print(check(visit))