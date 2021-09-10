import sys

dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]

def fun_func(a,b,c):
    if a<0 or b<0 or c<0:
        return 1

    elif a>20 or b>20 or c>20:
        return fun_func(a,b,c)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a<b<c:
        dp[a][b][c] = fun_func(a,b,c-1)+fun_func(a,b-1,c-1) - fun_func(a,b-1,c)

    else:
        dp[a][b][c] = fun_func(a-1,b,c)+fun_func(a-1,b-1,c)+fun_func(a-1,b,c-1)
        - fun_func(a-1,b-1,c-1)

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break

    print("w({},{},{}) = {}".format(fun_func(a,b,c)))

