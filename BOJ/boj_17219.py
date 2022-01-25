import sys


n,m = map(int,sys.stdin.readline().split())
pwd = {}

for _ in range(n):
	site,pword = sys.stdin.readline().split()
	pwd[site]=pword
	
for _ in range(m):
	ste = sys.stdin.readline().rstrip()
	print(pwd[ste])
	
			
	
