import sys
a,p = map(int,sys.stdin.readline().split())
answer= [a]
sum = 0
index=0
first_index= 0
for val in answer:
    val = str(val)
    sum = 0
    for v in val:
        sum+= int(v)**p

    if sum in answer:
        first_index = answer.index(sum)
        break
    answer.append(sum)
    index+=1


print(len(answer[:first_index]))


