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

##
INF = float('inf')
def solution(n, s, a, b, fares):
    answer = 2e9
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for x,y,w in fares:
        graph[y][x]=w
        graph[x][y]=w
    for i in range(1, n+1):
        graph[i][i] = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[j][i] = min(graph[j][i], graph[j][k]+graph[k][i])
    for t in range(1, n+1):
        tmp = graph[s][t] + graph[t][a]  + graph[t][b] 
        answer = min(tmp, answer)
    return answer