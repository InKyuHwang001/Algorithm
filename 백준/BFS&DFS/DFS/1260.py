
def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(n):
        if not visited[next] and graph[idx][next]:
            dfs(next)

n, m, v = map(int, input().split())
graph = [[False] * n for _ in range(n)]

for _ in range(m):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = True
    graph[x - 1][y - 1] = True

visited = [[False] * (n+1)]


dfs(v-1)