n, m = map(int, input().split())
graph = [input() for _ in range(n)]

visited= [[False]*m for _ in range(n)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]

ans = 0
tmp = [graph[0][0]]


def dfs(visited, tmp, y, x):
  global ans
  ans = max(ans, len(tmp))
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0<= ny <n and 0<= nx <m and not visited[ny][nx] and graph[ny][nx] not in tmp:
      visited[ny][nx] = True
      tmp.append(graph[ny][nx])
      dfs(visited, tmp, ny, nx)
dfs(visited, tmp, 0, 0)
print(ans)