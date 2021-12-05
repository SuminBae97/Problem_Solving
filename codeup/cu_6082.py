n = int(input())

check = ["3","6","9"]
for val in range(1,n+1):
    flag = False
    val = str(val)

    for c in check:
        if c in val:
            flag=True

    if flag:
        print("X",end=" ")
    else:
        print(val,end=" ")
