from collections import deque

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dy = [1,0,-1,0]
dx = [0,1,0,-1]

q = deque()

for y in range(N):
  for x in range(M):
    if graph[y][x] == 1:
      q.append([y,x])

while q:
  ey, ex = q.popleft()
  for i in range(4):
    ny = dy[i] + ey
    nx = dx[i] + ex
    if 0<= ny < N and 0<= nx < M and graph[ny][nx] == 0:
      graph[ny][nx] = graph[ey][ex] + 1
      q.append([ny, nx])

ans = 0

for y in range(N):
  for x in range(M):
    if graph[y][x] == 0:
      ans = -1
    if ans != -1:
      ans = max(ans, graph[y][x] -1)
print(ans)