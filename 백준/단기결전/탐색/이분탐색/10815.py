N = int(input())
Nnums = list(map(int, input().split()))
Nnums.sort()

M = int(input())
Mnums = list(map(int, input().split()))

for num in Mnums:
  s, e = 0, N-1
  tmp = 0
  while s<=e:
    m = (s + e)//2
    if Nnums[m] == num:
      tmp = 1
      break
    elif Nnums[m] < num:
      s = m + 1
    else:
      e = m -1
  print(tmp, end=" ")