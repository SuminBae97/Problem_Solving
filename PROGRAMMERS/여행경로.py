from collections import defaultdict

def solution(tickets):
    answer=[]
    graph = defaultdict(list)
    for dept, arrv in sorted(tickets):
        graph[dept].append(arrv)
    stack=[]
    def dfs(start):
        #stack.append(start)
        while graph[start]:
            dfs(graph[start].pop(0))
            # val = graph[start].pop(0)
        stack.append(start)
    dfs("ICN")

    stack = stack[::-1]
    return stack


tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))



