from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (n + 1)

q = deque()
q.append(1)

while q:
  now = q.popleft()
  for new in graph[now]:
    if visited[new] == 0:
      visited[new] = now
      q.append(new)

for idx in range(2, n+1):
  print(visited[idx])