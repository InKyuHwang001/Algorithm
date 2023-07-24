# 1966 프린터 큐

from collections import deque

t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  q=deque(map(int, input().split()))  
  cnt = 0
  while q:
    max_value = max(q)
    en = q.popleft()
    m -= 1
    if max_value == en:
      cnt += 1
      if m < 0:
        print(cnt)
        break
    else:
      q.append(en)
      if m < 0:
        m = len(q) - 1