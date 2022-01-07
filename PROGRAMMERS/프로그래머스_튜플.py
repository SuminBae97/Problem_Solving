

def solution(s):
	s = s[2:-2].split("},{")
	ans=[]
	for val in s:
		tmp = val.split(",")
		tmp_arr=[]
		for v in tmp:
			v = int(v)
			tmp_arr.append(v)
		ans.append(tmp_arr)	
			
	ans.sort(key=lambda x:len(x))
	fa=[]
	
	for val in ans:
		for vv in val:
			if vv not in fa:
				fa.append(vv)
	return fa		
