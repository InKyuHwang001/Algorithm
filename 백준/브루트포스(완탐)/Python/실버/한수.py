# 한수 1065

n = int(input())
tmp = 0
for i in range(1, n + 1):
  if i < 100:
    tmp += 1
  else:
    li = list(map(int, str(i)))
    if li[2] - li[1] == li[1] - li[0]:
      tmp += 1
print(tmp)

## 1000이상 수의 방법
def sol(li):
  for i in range(len(li) - 1):
    if li[i] - li[i + 1] != li[i + 1] - li[i + 2]:
      return 0
  else: 
    return 1

n = int(input())
tmp = 0
for i in range(1, n + 1):
  if i < 100:
    tmp += 1
  else:
    li = list(map(int, str(i)))
    tmp += sol(li)
print(tmp)