import heapq

N = int(input())
M = int(input())

graph = [[]for _ in range(N+1)]
chk = [False] *(N+1)
rs = 0

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append([c, b])
  graph[b].append([c, a])

heap = [[0,1]]
while heap:
  w, en = heapq.heappop(heap)
  if chk[en] == False:
    chk[en] = True
    rs += w
    for ne in graph[en]:
      if chk[ne[1]] == False: #없어도 됨
        heapq.heappush(heap, ne)
print(rs)