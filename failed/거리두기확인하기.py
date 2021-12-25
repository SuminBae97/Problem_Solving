from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(place,x,y):
    q = deque()
    visited = [[False] * 5 for _ in range(5)]
    q.append((x,y,0))
    visited[x][y] = True

    while q:
        xp,yp,dp = q.popleft()

        if place[xp][yp]=="P" and 0< dp <3:
            return False
        # 이미 만족
        if dp >=3:
            break

        for i in range(4):
            nx = xp+dx[i]
            ny = yp+dy[i]
            if nx<0 or nx>=5 or ny<0  or ny>=5:
                continue
            elif place[nx][ny]!="X" and visited[nx][ny]!=True:
                q.append((nx,ny,dp+1))
                visited[nx][ny]=True
    return True



def solution(places):
    answer = []
    for place in places:
        chk = 0
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j]=="P":
                    if not bfs(place,i,j):
                        answer.append(0)
                        chk=1
                        break
            if chk:
                break
        else:
            answer.append(1)

    return answer

#
places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))