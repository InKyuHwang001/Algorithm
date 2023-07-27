# 10709 기상캐스터
h, w = map(int, input().split())
graph = [list(map(str, ' '.join(input()).split())) for _ in range(h)]

for y in range(h):
  tmp = -1
  for x in range(w):
    if tmp != -1:
      tmp += 1
    if graph[y][x] == 'c':
      tmp = 0
    graph[y][x] = tmp

for y in graph:
  for i in y:
    print(i, end=' ')
  print()