

n=int(input("test case num:"))

for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    r=((x1-x2)**2+(y1-y2)**2)**(1/2) #두직선사이의 거리

    radius=[r1,r2,r]
    m=max(radius)
    radius.remove(m)

    if r1==r2 and r==0:
        print(-1)
    elif r==(r1+r2) or m==sum(radius):
        print(1)

    elif m>sum(radius):
        print(0)
    else:
        print(2)


















