from itertools import permutations
n,m = map(int, input().split())
arr = list(permutations(range(1,n+1), m))
for a in arr:
  print(*a)