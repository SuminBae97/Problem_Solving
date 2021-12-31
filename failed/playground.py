from collections import deque
import sys



start,target = map(int,sys.stdin.readline().split())
MAX=200000
visited = [False]*(MAX+1)
dst = [0]*(MAX+1)

def bfs(start,target,dst,visited):
    q = deque()
    q.append(start)
    visited[start]=True

    while q:
        val = q.popleft()

        for vv in [val+1,val-1,val*2]:
            if vv>MAX or vv<0:
                continue
            else:
                if visited[vv]==False:
                    q.append(vv)
                    visited[vv]=True
                    dst[vv] = dst[val]+1


bfs(start,target,dst,visited)
print(dst[target])

