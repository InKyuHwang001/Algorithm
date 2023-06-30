# RGB거리 1149

n = int(input())
rgbs = [list(map(int, input().split())) for _ in range(n)]


for i in range(1, n):
  rgbs[i][0] += min(rgbs[i - 1][1], rgbs[i - 1][2]) 
  rgbs[i][1] += min(rgbs[i - 1][0], rgbs[i - 1][2])
  rgbs[i][2] += min(rgbs[i - 1][1], rgbs[i - 1][0])

print(min(rgbs[-1]))