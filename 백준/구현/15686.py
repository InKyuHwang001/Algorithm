"""
이분, 백트, bfs, dp 중 뭐지 고민 후 시작하기

여러게중 조합을 구하는 것이기에 백트
"""
from itertools import combinations as comb

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 1e9

houses = []
chicks = []
for y in range(n):
  for x in range(n):
    if graph[y][x] == 1:
      houses.append([y, x])
    elif graph[y][x] == 2:
      chicks.append([y, x])

selectedChicksArr = list(comb(chicks, m))

maxrich = 2*n

for scs in selectedChicksArr:
  tmp = 0
  for house in houses:
    guri = maxrich 
    for sc in scs:
      rich = abs(house[0]-sc[0])+ abs(house[1]-sc[1])
      guri = min(guri, rich)
    tmp += guri
  ans = min(tmp, ans)
print( ans)
