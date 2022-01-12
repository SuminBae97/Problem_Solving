import sys
n= int(sys.stdin.readline())

seq = list(map(int,sys.stdin.readline().split(" ")))
dp = [1]*(n+1)

for i in range(n):
	for j in range(i):
		if seq[i]>seq[j]:
			dp[i] = max(dp[i],dp[j]+1)

print(max(dp))			

'''answer=[0]

for val in seq:
	if answer[-1]< val:
		answer.append(val)

	else:
		left = 0
		right = len(answer)
		
		while left<right:
			mid = (left+right)//2
			
			if answer[mid] < val:
				left = mid+1
			else:
				right = mid
		answer[right] = val		
			
print(len(answer)-1)	'''

	
