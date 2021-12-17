 			 				 			 				 			 	

def solution(n,words):
	turn =0
	person =0 
	appeared =[words[0]]
	for i in range(1,len(words)):
		
		print(words[i][0])
		print(words[i-1][-1])
		
		if words[i][0]!=words[i-1][-1]:
			turn = (i//n)+1
			person = (i%n)+1
			break
		
		elif words[i] not in appeared:
			appeared.append(words[i])
		
				
		else:
			turn =  (i//n)+1
			person = (i%n)+1
			break	
	
	return [person,turn]
	
print(solution(n,words))	

