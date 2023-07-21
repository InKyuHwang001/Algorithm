# 10819 차이를 최대로

##이터툴
from itertools import permutations as P

n = int(input())
nums = list(map(int, input().split()))

arr = list(P(nums, n))

ans = 0
for ar in arr:
  tmp = 0
  for i in range(1, n):
    tmp += abs(ar[i - 1] - ar[i])
  ans = max(ans, tmp)
print(ans)

##백트래킹
n = int(input())
nums = list(map(int, input().split()))
visited = [False]*n

ans = 0
def sol(li):
  global ans
  if len(li) == n:
    tmp =0
    for i in range(n-1):
      tmp += abs(li[i] - li[i+1])
    ans = max(ans, tmp)
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      li.append(nums[i])
      sol(li)
      visited[i] = False
      li.pop()

sol([])
print(ans)