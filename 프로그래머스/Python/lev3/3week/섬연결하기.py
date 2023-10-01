from heapq import heappop, heappush
def solution(n, costs):
    ans = 0
    cost_all = [[]for _ in range(n)]
    chk = [False] * n
    heap = []
    heappush(heap,[0,0])
    
    for s, e, w in costs:
        cost_all[s].append([w,e])
        cost_all[e].append([w,s])
        
    while heap:
        w, s =heappop(heap)
        if chk[s] == False:
            chk[s] = True
            ans += w
            for cost in cost_all[s]:
                heappush(heap, cost)
    return ans