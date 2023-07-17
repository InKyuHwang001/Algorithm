#15651 N과 M(3)

##itertools
from itertools import product

n, m =  map(int, input().split())
num = [i for i in range(1, n+1)]

arr = list(product(num, repeat = m))
arr.sort()

for i in arr:
  print(" ".join(map(str, i)))

##backtracking
n, m =  map(int, input().split())
s = []
def sol():
  if len(s) == m:
    print(" ".join(map(str, s)))
    return
  else:
    for i in range(1, n+1):
      s.append(i)
      sol()
      s.pop()
sol()