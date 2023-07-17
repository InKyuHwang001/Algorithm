#15651 N과 M(4)

##itertools
from itertools import combinations_with_replacement as comb

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

arr = list(comb(num, m))
for i in arr:
  print(' '.join(map(str, i)))

##backtracking
n,m = map(int, input().split())
s = []

def sol(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(start, n+1):
        s.append(i)
        sol(i)
        s.pop()
    
sol(1)