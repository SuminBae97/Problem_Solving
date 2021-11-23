import sys
n = int(input())


dp=[0]*(100000)

price = list(map(int,sys.stdin.readline().split()))
price.insert(0,0)

dp[1] = price[1]

for i in range(2,n+1):
		tmp=[]
		for j in range(1,i+1):
			tmpd = price[j]+dp[i-j]
			tmp.append(tmpd)	
		dp[i] = max(tmp)
print(dp[n])		
