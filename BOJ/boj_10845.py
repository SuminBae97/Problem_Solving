import sys
from collections import deque
n = int(input())

q = deque()

def push(x):
	q.append(x)
	
	
def front():
	if q:
		return q[0]
	
	else:
		return -1	

def rear():
	if q:
		return q[-1]
	
	else:
		return -1
			
def empty():
	if q:
		return 0
	
	else:
		return 1
		
def pop():
	if q:
		return q.popleft()
	else:
		return -1
			
def size():
	return len(q)						
	
	
	
for _ in range(n):
	command = sys.stdin.readline().split()
	
	if command[0]=="push":
		push(int(command[1]))
	
	elif command[0]=="front":
		print(front())
	elif command[0]=="back":
		print(rear())
	elif command[0]=="size":
		print(size())
	elif command[0]=="pop":
		print(pop())
	elif command[0]=="empty":
		print(empty())					
