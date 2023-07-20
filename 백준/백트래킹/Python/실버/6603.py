# 6603 로또

## itertools
from itertools import combinations as cb
while True:
  tmp_arr = list(map(int, input().split()))
  if tmp_arr == [0]:
    break
  nums = tmp_arr[1:]
  ans_list = list(cb(nums, 6))
  for ans in ans_list:
    print(" ".join(map(str, ans)))
  print()


##backtracking
def sol(cnt):
  if len(s) == 6:
    print(' '.join(map(str, s)))
  for i in range(cnt, n+1):
    if nums[i] not in s:
      s.append(nums[i])
      sol(i+1)
      s.pop()
      
while True:
  nums = list(map(int, input().split()))
  n = nums[0]
  if n == 0:
    break
  s = []
  sol(1)
  print()