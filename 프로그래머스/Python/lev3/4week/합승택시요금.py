import heapq
def solution(n, s, a, b, fares):

    ans = 200000001
    graph = [[] for _ in range(n+1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))
    
    dist = [[]]
    for i in range(1, n+1):
        res = [1e9 for _ in range(n+1)]
        res[i] = 0
        q = []
        heapq.heappush(q, (res[i], i))
        while q:
            result_x, x = heapq.heappop(q)
            for fu, fw in graph[x]:
                if res[fu] > result_x + fw:
                    res[fu] = result_x + fw
                    heapq.heappush(q, ([res[fu], fu]))
        dist.append(res)
 
    for i in range(1, n+1):
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])
    return ans