
from collections import Counter

def solution(str1,str2):
	str1_low = str1.lower()
	str2_low = str2.lower()
    
	str1_lst = []
	str2_lst = []

    
	for i in range(len(str1_low)-1):
			
	    if str1_low[i].isalpha() and str1_low[i+1].isalpha():
	        str1_lst.append(str1_low[i] + str1_low[i+1])
	for j in range(len(str2_low)-1):
	    if str2_low[j].isalpha() and str2_low[j+1].isalpha():
	        str2_lst.append(str2_low[j] + str2_low[j+1])
	
	c1 = Counter(str1_lst)
	c2 = Counter(str2_lst)


	intersect = dict()
	tot = dict()
	
	for val in c1.keys():
		if val in c2.keys():
			intersect[val] = min(c2[val],c1[val])
			tot[val] = max(c1[val],c2[val])
		else:
			tot[val] = c1[val]	
	
	for v2 in c2.keys():
		if v2 not in tot.keys():
			tot[v2] = c2[v2]
	
	i_sum=0
	t_sum=0
	
	if len(intersect)==0 and len(tot)==0:
		return 1
	
	for value in intersect.values():
		i_sum+=value
	
	for v in tot.values():
		t_sum+=v
		
	return int((i_sum/t_sum)*65536)											
	
#s1='aa1+aa2'	
#s2='AAAA12'		

s1='E=M*C^2'	
s2='e=m*c^2'	
print(solution(s1,s2))	




