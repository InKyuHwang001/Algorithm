from collections import deque
import sys
ff = sys.stdin.readline

N, M, K, X = map(int, ff().split()) #도시수, 도로수, 거리정보, 출발정보

cities = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, ff().split())
  cities[a].append(b)

chk = [False] * (N+1)
ans = []
q = deque()
q.append((0,X))
chk[X] = True

while q:
  dis, now = q.popleft()
  if dis == K:
    ans.append(now)
  else:
    dis += 1
    for nn in cities[now]:
      if chk[nn] == False:
        q.append((dis, nn))
        chk[nn] = True

if ans == []:
  print(-1)
else:
  ans.sort()
  for a in ans:
    print(a)


import heapq
import sys
f = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k: answer.append(i)

if len(answer) == 0: print(-1)
else:
    for i in answer: print(i, end='\n')