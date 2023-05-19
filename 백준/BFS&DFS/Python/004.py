#유기농 배추

t = int(input())
n, m, k = map(int, input().split())
graph  = [[0] * m for _ in range(n)]

for _ in range(k):
  y, x = map(int, input().split())
  graph[y][x] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

##bfs
from collections import deque
q = deque()
for _ in range(t):
    ans = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] != 0:
                ans += 1
                q.append([a, b])
                while q:
                    y, x = q.popleft()
                    graph[y][x] = 0
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0 <= ny < n and 0<= nx < m and graph[ny][nx] != 0:
                            q.append([ny, nx])  
    print(ans)

##dfs
ans = 0

def dfs(y, x):
  graph[y][x] = 0
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < n and 0<= nx < m and graph[ny][nx] != 0:
      dfs(ny, nx)
for _ in range(t):
  for a in range(n):
    for b in range(m):
      if graph[a][b]:
        dfs(a, b)
        ans += 1
  print(ans)