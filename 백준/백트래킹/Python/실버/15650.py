#15650 N과 M(2)

##itertools
from itertools import combinations as comb

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

arr = list(comb(num, m))
arr.sort()

for i in arr:
  print(' '.join(map(str, i)))

##backtracking
n, m = map(int, input().split())
s = []
def sol(cnt):
  if len(s) == m:
    print(' '.join(map(str, s)))
  for i in range(cnt, n+1):
    if i not in s:
      s.append(i)
      sol(i+1)
      s.pop()
sol(1)