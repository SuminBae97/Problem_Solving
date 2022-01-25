import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
m = int(input())
chk = list(map(int,sys.stdin.readline().split()))
arr.sort()

def b_search(target,arr):
	left = 0
	right = len(arr)-1
	
	while left<=right:
		mid = (left+right)//2
		
		if arr[mid]==target:
			return 1 
		
		elif arr[mid]<target:
			left = mid+1
			
		else:
			right = mid-1		  
	
	return 0	

for val in chk:
	print(b_search(val,arr))	
	
