
def solution(phone_book):
    flag=True
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                flag=False
            if phone_book[j].startswith(phone_book[i]):
                flag=False
    return flag            
