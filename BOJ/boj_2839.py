import sys

n = int(sys.stdin.readline())

count =0
while n>0:
    tmp = n
    if tmp%5==0:
        count +=(tmp//5)
        n = n%5

    else:
        count+=1
        n = n-3

if n!=0:
    print(-1)

else:
    print(count)