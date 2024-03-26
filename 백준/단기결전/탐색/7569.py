from collections import deque

M, N, H = map(int, input().split()) #X,Y, Z

graph = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]

q = deque()
for z in range(H):
  for y in range(N):
    for x in range(M):
      if graph[z][y][x] == 1:
        q.append((z,y,x))

dy = [0,1,0,-1,0,0]
dx = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]

while q:
  ez,ey,ex = q.popleft()
  for i in range(6):
    nz = ez + dz[i]
    ny = ey + dy[i]
    nx = ex + dx[i]
    if nz < 0 or nz >= H:
      continue
    if ny < 0 or ny >= N:
      continue
    if nx < 0 or nx >= M:
      continue
    if graph[nz][ny][nx] == 0:
      graph[nz][ny][nx] = 1+ graph[ez][ey][ex]
      q.append((nz,ny,nx))

ans = 0
zero = False

for z in range(H):
  for y in range(N):
    for x in range(M):
      if graph[z][y][x] == 0:
        zero = True
        break
      ans = max(ans, graph[z][y][x])
print(-1 if zero else ans -1)