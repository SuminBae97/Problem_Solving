import sys

n=int(sys.stdin.readline())
bnum = 0b1
dnum = int(format(bnum,'b'),10)


while 1:
	if dnum%n ==0:
		print(dnum)
		break
	bnum+=1
	dnum = int(format(bnum,'b'),10)
	
	if dnum>=100000000000000000000: 
		print(0) 
		break
		
