from itertools import permutations,combinations
from collections import Counter

def solution(orders,course):
	answer=[]
	
	for num_ord in course:		
		total_order=[]
		for val in orders:
			tmp = list(combinations(val,num_ord))
			for v in tmp:
				v = sorted(v)
				t = ''.join(v)
				total_order.append(t)
				
				
		ct = Counter(total_order)
		if len(ct)==0:
			break
		else:
			max_val = (ct.most_common(1)[0][1])
		
		for key,value in ct.items():
			if value==1:
				continue
			if value==max_val:
				answer.append(key)
	
	answer.sort()	
	return answer
					
		
	
	

