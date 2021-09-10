import sys
sugar = int(sys.stdin.readline())

def solution(n):
    bags=0
    while True:
        if n==0:
            break

        if n%5==0:
            bags +=(n//5)
            break
        elif n<0:
            return -1
        n-=3
        bags+=1

    return bags
print(solution(sugar))