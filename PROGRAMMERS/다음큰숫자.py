def solution(n):
    hx = bin(n)[2:]
    b = n+1
    hxb = bin(b)[2:]

    while hxb.count('1') != hx.count('1'):
        b = b + 1
        hxb = bin(b)[2:]

    return b

