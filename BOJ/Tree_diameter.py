import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e4))
n = int(sys.stdin.readline().rstrip())
tree =defaultdict(list)

for i in range(n-1):
    x,y,w = map(int,sys.stdin.readline().rsplit())
    tree[x].append((y,w))


def solve(node,cost):
    if not tree[node]:
        return cost

    total=0
    m=0

    for next_node,w in tree[node]:
        m = solve(next_node,cost+w)