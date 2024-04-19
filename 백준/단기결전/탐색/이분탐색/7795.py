T = int(input())
for _ in range(T):
  
  N, M = map(int, input().split())
  
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  A.sort()
  B.sort()

  cnt = 0

  for a in A:
    s, e = 0, M
    while s<e:
      m = (s+e)//2
      if a <= B[m]:
        e = m
      else:
        s = m + 1
    cnt += e 
  print(cnt)
