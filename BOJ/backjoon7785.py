
n=int(input())

attend={}

for i in range(n):
    a,b=input().split()
    attend[a]=b

result=[]

for k,v in attend.items():
    if v=='enter':
        result.append(k)

result.sort(reverse=True)
for i in range(len(result)):
    print(result[i])




