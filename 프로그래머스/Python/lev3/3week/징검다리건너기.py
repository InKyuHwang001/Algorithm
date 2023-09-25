from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[]for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visited = [-1] * (n+1)
    visited[1] = 0
    q = deque()
    q.append(1)
    
    while q:
        en = q.popleft()
        for next in graph[en]:
            if visited[next] == -1:
                visited[next] = visited[en] + 1
                q.append(next)
    visited.sort(reverse=True)
    answer = visited.count(visited[0])
    return answer