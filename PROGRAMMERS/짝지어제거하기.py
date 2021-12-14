		
		
def solution(s):
	s = list(s)
	f = s.pop(0)
	stack = [f]

	while s:
		val = s.pop(0)
		
		if len(stack)==0:
			stack.append(val)
			
		elif val==stack[-1]:
			stack.pop(-1)
		
		else:
			stack.append(val)
			
	if len(stack)==0:
		return 1
	
	else:
		return 0					
#### sol1 test case pass but efficiency test failed																 

def solution(s):
	stack =[]
	for i in s:
		if len(stack)==0:
			stack.append(i)
		elif stack[-1]==i:
			stack.pop()
		else:
			stack.append(i)
	
	if len(stack)==0:
		return 1
	else:
		return 0								
