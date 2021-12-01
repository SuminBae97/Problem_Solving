n = int(input())
ans=[]
for _ in range(n):
    tmp = int(input())
    ans.append(tmp)

#sorted nlogn
# sort() nlogn
# 내장 라이브러리 사용시 pypy3로 하는게 효율성 측면에서
ans = sorted(ans)
#ans.sort()
for val in ans:
    print(val)
