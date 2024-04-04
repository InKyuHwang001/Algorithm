## 실패 
### 위상정렬을 넣지 않음
import sys
import heapq
N, M = map(int, sys.stdin.readline().rstrip().split())

tmp = []

heap = []
for _ in range(M):
  a,b = map(int, sys.stdin.readline().rstrip().split())
  heapq.heappush(heap, (a, b))
  tmp.append(a)
  tmp.append(b)

for num in range(1, N+1):
  if num not in tmp:
    heapq.heappush(heap, (num, -1))
ans = []
while heap:
  now, next = heapq.heappop(heap)
  ans.append(now)
  if next != -1:
    heapq.heappush(heap,(next, -1))

print(*ans)

##성공
### 위상정렬 적용
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())

  in_degree[b] += 1
  graph[a].append(b)

heap = []
for i in range(1, n + 1):
  if in_degree[i] == 0:
    heapq.heappush(heap, i)

while heap:
  now = heapq.heappop(heap)
  print(now, end=" ")
  for g in graph[now]:
    in_degree[g] -= 1
    if in_degree[g] == 0:
      heapq.heappush(heap, g)