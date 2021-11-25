#print(ord('a'))
#print(chr(97))

al={}
for i in range(26):
	al[chr(i+97)]=-1
	
	
s = input()
s = list(s)


for val in s:
	al[val] = s.index(val)
	
for val in al.values():
	print(val, end=" ")
