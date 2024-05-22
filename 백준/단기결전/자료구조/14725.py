DASH = "--"
N = int(input())

foods = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  foods.append(tmp[1:])

foods.sort()

ans = []

for i in range(N):
  if i == 0:
    for j in range(len(foods[i])):
      ans.append(DASH * j + foods[i][j])
  else:
    idx = 0
    for j in range(len(foods[i])):
      if foods[i-1][j] != foods[i][j] or len(foos[i-1]) <= j:
        break
      else:
        idx = j + 1
    for j in range(idx, len(foods[i])):
      ans.append(DASH * j + foods[i][j])

for a in ans:
  print(ans)