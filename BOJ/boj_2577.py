import sys
from collections import Counter
ct={}

for i in range(10):
    ct[str(i)]=0

a =int(sys.stdin.readline())
b =int(sys.stdin.readline())
c =int(sys.stdin.readline())
answer=a*b*c
answer=str(answer)

for s in answer:
    ct[s]+=1

for val in ct.values():
    print(val)