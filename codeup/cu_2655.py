import sys

a,b = map(int,sys.stdin.readline().rsplit())
print(format(-b/a,'.4f'))