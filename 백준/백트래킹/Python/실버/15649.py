# n과 m
## 이터툴 
from itertools import permutations

n, m  = map(int, input().split())
nums = [i for i in range(1, n+1)]

arr = permutations(nums, m)
for i in arr:
  print(' '.join(map(str, i)))

## 백트래킹
n, m  = map(int, input().split())
s = []

def sol():
  if len(s) == m:
    print(' '.join(map(str, s)))    
  for i in range(1, n+1):
    if i not in s:
      s.append(i)
      sol()
      s.pop()
sol()