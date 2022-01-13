import sys
n= int(sys.stdin.readline())
seq = list(map(int,sys.stdin.readline().split()))
seq.reverse()

answer=[0]
for val in seq:
	if answer[-1]<val:
		answer.append(val)
		
	else:
		left =0
		right = len(answer)
		
		while left<right:
			mid = (left+right)//2
			
			if answer[mid]<val:
				left = mid+1
			else:
				right = mid
		answer[right] =val

print(len(answer)-1)						




