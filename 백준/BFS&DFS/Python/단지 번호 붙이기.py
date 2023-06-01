#단지 번호 붙이기

n = int(input())
graph = [list(map(int, " ".join(input()).split())) for _ in range(n)]
ans = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#bfs
from collections import deque

q = deque()
tmp = 1
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      tmp += 1
      graph[i][j] = tmp
      cnt = 1
      q.append([i, j])
      while q:
        y, x = q.popleft()
        for k in range(4):
          ny = dy[k] + y
          nx = dx[k] + x
          if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1:
            cnt += 1
            graph[ny][nx] = tmp
            q.append([ny, nx])
      ans.append(cnt)

print(tmp -1)
ans = sorted(ans)
for i in range(tmp -1):
  print(ans[i])

#dfs
tmp = 0

def dfs(y, x):
  global cnt
  if 0 <= y < n and 0 <= x < n and graph[y][x] == 1:
      cnt += 1
      graph[y][x] = 0
      for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]
         dfs(ny, nx)
  else:
    return False

cnt = 0
result = 0
for y in range(n):
  for x in range(n):
    if dfs(y, x) != False:
      ans.append(cnt)
      tmp += 1
      cnt = 0

ans.sort()
print(tmp)
for i in range(len(ans)):
    print(ans[i])