from collections import deque
INF = 1e9
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 1
while True:
  N = int(input())
  if N == 0:
    break
  graph = [list(map(int, input().split())) for _ in range(N)]
  
  distance = [[INF]*N for _ in range(N)]
  
  q = deque()
  q.append((0,0)) 
  distance[0][0] = graph[0][0]
  
  while q:
    ey, ex = q.popleft()
    dis = distance[ey][ex]
    for i in range(4):
      ny = ey + dy[i]
      nx = ex + dx[i]

      if ny < 0 or ny >= N:
        continue
      if nx < 0 or nx >= N:
        continue
      ndis = dis + graph[ny][nx]
      if distance[ny][nx] > ndis:
        distance[ny][nx] = ndis
        q.append((ny,nx))
  print("Problem "+ str(cnt)+": "+str(distance[N-1][N-1]))
  cnt += 1

#################
import heapq

INF = int(1e9)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 1

while True:
  n = int(input())
  if n == 0:
    break

  graph = [list(map(int, input().split())) for _ in range(n)]
  distance = [[INF] * n for _ in range(n)]

  heap = []
  heapq.heappush(heap, (graph[0][0], 0, 0))
  distance[0][0] = 0
  while heap:
    cost, ey, ex = heapq.heappop(heap)
    if ey == n - 1 and ex == n - 1:
      print(f'Problem {cnt}: {distance[ey][ex]}')
      break
      
    
    for i in range(4):
      nx = ex + dx[i]
      ny = ey + dy[i]
      if ny < 0 or ny >= n:
        continue
      if nx < 0 or nx >= n:
        continue
      
      ncost = cost + graph[ny][nx]
      if ncost < distance[ny][nx]:
        distance[ny][nx] = ncost
        heapq.heappush(heap, (ncost, ny, nx))
  cnt += 1
