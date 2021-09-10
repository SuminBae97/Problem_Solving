from itertools import combinations
from functools import reduce

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

def solution(clothes):
    dic={}






clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
#clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes))
