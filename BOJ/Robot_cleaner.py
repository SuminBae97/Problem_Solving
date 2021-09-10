from sys import stdin
from collections import deque
n,m = map(int,stdin.readline().split())
r,c,d = map(int,stdin.readline().split())

matrix = [list(map(int,stdin.readline().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]






def boundary_check(x,y):
    return True if 0<=x and x<n and 0<=y and y<m else False

def change_direction(d):
    return d-1 if d!=0 else 3

def go_back(d):
    return (d+2)%4


def clean(r,c,d):
    q = deque([[r,c]])
    matrix[r][c]=2
    count=1

    while q:
        x,y = q.popleft()

        for i in range(4):
            d = change_direction(d)
            nx = x+dx[d]
            ny = y+dy[d]

            if boundary_check(nx,ny) and matrix[nx][ny]==0:
                q.append([nx,ny])
                count+=1
                matrix[nx][ny]=2
                break

            if i==3:
                nx,ny = x+dx[go_back(d)] , y+dy[go_back(d)]
                q.append([nx,ny])

                if matrix[nx][ny]==1:
                    return count

print(clean(r,c,d))