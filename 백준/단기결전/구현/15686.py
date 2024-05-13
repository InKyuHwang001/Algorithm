from itertools import combinations as comb

HOSE = 1
CHICK = 2

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chicks = []
hoses = []
for y in range(N):
  for x in range(N):
    if graph[y][x] == CHICK:
      chicks.append((y, x))
    elif graph[y][x] == HOSE:
      hoses.append((y, x))
ans = N**3

for cand in list(comb(chicks, M)): 
  tmp = []
  for hy, hx in hoses:
    tmp.append(min(abs(hy - cy) + abs(hx - cx) for cy, cx in cand))
  ans = min(ans, sum(tmp))
print(ans)