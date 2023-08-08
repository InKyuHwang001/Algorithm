#수리공 항승 1449

n, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

cnt = 1
start = data[0]

for location in data[1:]:
  if location in range(start, start+l):
    continue
  else:
    start = location
    cnt += 1

print(cnt)