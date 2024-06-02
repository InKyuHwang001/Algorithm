import heapq

V, E = map(int, input().split())
graph = [[]for _ in range(V+1)]

ans = 0
chk =[False] * (V + 1)

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append([c, b])
  graph[b].append([c, a])

heap = []

heapq.heappush(heap, [0, 1])

while heap:
  cnt, now = heapq.heappop(heap)
  if chk[now] == False:
    chk[now] = True
    ans += cnt
    for tmp in graph[now]:
        if chk[tmp[1]] == False:
          heapq.heappush(heap, tmp) 

print(ans)