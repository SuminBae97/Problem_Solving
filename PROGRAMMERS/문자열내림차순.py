def solution(s):
	answer=''
	sindex = [ord(val) for val in s]
	sindex = sorted(sindex,reverse=True)
	
	for val in sindex:
		answer+=chr(val)

	        
	return answer    
	
