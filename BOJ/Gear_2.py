import sys
from collections import deque
gear={}
t = int(sys.stdin.readline())

for i in range(t):
    gear[i+1] = deque(list(map(int,sys.stdin.readline().rstrip())))

k = int(sys.stdin.readline())

def check_right(start,dirs):
    if start>t or gear[start-1][2]== gear[start][6]:
        return

    if gear[start-1][2]!=gear[start][6]:
        check_right(start+1,-dirs)
        gear[start].rotate(dirs)

def check_left(start,dirs):
    if start<1 or gear[start][2]== gear[start+1][6]:
        return

    if gear[start][2]!=gear[start+1][6]:
        check_left(start-1,-dirs)
        gear[start].rotate(dirs)


for _ in range(k):
    start,dirs = map(int,sys.stdin.readline().split())
    check_left(start-1,-dirs)
    check_right(start+1,-dirs)
    gear[start].rotate(dirs)


count=0

for val in gear.values():
    if val[0]==1:
        count+=1
print(count)

