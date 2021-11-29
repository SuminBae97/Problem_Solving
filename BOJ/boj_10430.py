import sys
a,b,c = map(int,sys.stdin.readline().split())
print(a,b,c)
#(A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를

r1 = (a+b)%c
r2 = ((a%c)+(b%c))%c
r3 = (a*b)%c
r4 = ((a%c)*(b%c))%c
r = [r1,r2,r3,r4]
for val in r:
    print(val)