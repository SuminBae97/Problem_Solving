def solution(number,k):
	s=[]
	cnt = 0
	for i in number:
		if cnt==k:
			s.append(i)
			
		else:
			if not s:
				s.append(i)
			
			else:
				while s:
					if cnt==k or i<=s[-1]:
						break
					
					if i>s[-1]:
						s.pop()
						ct+=1
				s.append(i)
							
	while cnt!=k:
		s.pop()
		cnt+=1
	return ''.join(s)						
