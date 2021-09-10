import itertools
import sys

n,m=map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
# ncr = itertools.combinations(cards,3)
# ncr = itertools.combinations(cards,3)


answer = 0
for i in range(len(cards)):
    for j in range(i+1,len(cards)):
        for k in range(j+1,len(cards)):
            if cards[k]+cards[j]+cards[i] > m:
                continue

            else:
                answer = max(answer,cards[k]+cards[j]+cards[i])


print(answer)

# result = 0
# for a,b,c in ncr:
#     sumf = a+b+c
#     if sumf > m:
#         continue
#     else:
#         result = max(result,sumf)
#
# print(result)

