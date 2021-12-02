import heapq
import copy
    


def solution(scoville, K):
    answer = 0
    count=0
    heapq.heapify(scoville)
    try:
        
        while scoville[0]<K:
            l1 = heapq.heappop(scoville)
            l2 = heapq.heappop(scoville)
            l3 = l1+(2*l2)
            heapq.heappush(scoville,l3)
            count+=1
        return count    
    except:
        return -1
    


