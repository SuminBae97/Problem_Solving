from itertools import combinations,permutations
import sys

n,k = int(input()) , int(input())
card = []

for _ in range(n):
	card.append(input())

answer=set()	
for p in permutations(card,k):
		answer.add(''.join(p))
print(len(answer))		
