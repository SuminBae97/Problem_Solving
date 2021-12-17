#arr1= [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
#arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

def solution(arr1,arr2):
	transpose=[]
	for j in range(len(arr2[0])):
		tp =[]
		for i in range(len(arr2)):
			tp.append(arr2[i][j])
		transpose.append(tp)	
			
			
	answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
	
		
	for i in range(len(answer)):
		for j in range(len(answer[0])):
			sum=0
			for a,b in zip(arr1[i],transpose[j]):
				sum+=a*b	
				answer[i][j]=sum
		
	return answer	
		


