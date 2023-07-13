#토마토 7576

## 1차
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dy = [0,1,0,-1]
dx = [-1,0,1,0]

q = deque()
for x in range(n):
  for y in range(m):
    if graph[y][x] == 1:
      q.append([y,x,0])

ans = 0

while q:
  ey, ex, ecnt = q.popleft()
  for i in range(4):
    ny = ey + dy[i]
    nx = ex + dx[i]
    ncnt = ecnt + 1
    if 0<= ny < m and 0<= nx < n and graph[ny][nx] == 0:
      graph[ny][nx] = 1
      ans = max(ans, ncnt)
      q.append([ny, nx, ncnt])


for x in range(n):
  for y in range(m):
    if graph[y][x] == 0:
      ans = -1
      break
      
print(ans)

