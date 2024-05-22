import sys
input = sys.stdin.readline
N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]

points.sort()

ans = 0

s, e = points[0]
for i in range(1, N):
  if e >= points[i][1]:
    continue
  elif points[i][0] <= e < points[i][1]:
    e = points[i][1]
  elif e < points[i][0]:
    ans += e - s
    s = points[i][0]
    e = points[i][1]

ans += e - s
print(ans)