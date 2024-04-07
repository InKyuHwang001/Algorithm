N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  for y in range(N):
    for x in range(N):
      if graph[y][i] == 1 and graph[i][x] == 1:
        graph[y][x] = 1

for li in graph:
  print(*li)