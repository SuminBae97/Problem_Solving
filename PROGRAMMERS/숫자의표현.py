def solution(n):
	a = [i for i in range(1,n+1)]
	count = 0
	for i in range(len(a)):
		for j in range(0,len(a)):
			value = sum(a[i:i+j])
			
			if value==n:
				count+=1
				break
			elif value>n:
				break
	return count			
				
								
