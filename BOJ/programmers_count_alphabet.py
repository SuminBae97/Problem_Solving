from collections import Counter

def solution(s):
    s=s.lower()
    count_dic=Counter(s)
    
    if count_dic['p']==count_dic['y']:
        return True
    else:
        return False