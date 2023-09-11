def dfs(idx):
    global visited, result
    visited[idx] = True
    for next in range(1, n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
            result += 1
n = int(input())
m = int(input())

graph = [[False] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    y, x = map(int, input().split())
    graph[y][x] = True
    graph[x][y] = True

visited = [False] * (n + 1)

ans = 0
for i in range(1, n+1):
    if not visited[i]:
        result = 0
        dfs(i)
        ans = max(result, ans)
print(ans)

