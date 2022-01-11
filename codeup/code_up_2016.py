import sys

n = int(sys.stdin.readline())
num = list(map(str,sys.stdin.readline()))
ct = 0
num.reverse()
answer=[]

for v in num:
	if ct!=3:
		answer.append(v)
		ct+=1
	
	elif ct==3:
		answer.append(',')
		answer.append(v)
		ct=1
answ=''
for val in answer[::-1]:
	answ+=val
print(answ)					
