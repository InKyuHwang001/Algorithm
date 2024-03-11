from collections import deque

N, K = map(int, input().split())

q = deque([x for x in range(1, N+1)])
tmp = "<"
cnt = 0
while q:
  cnt += 1
  num = q.popleft()
  if cnt == K:
    tmp += str(num)+", "
    cnt = 0
  else:
    q.append(num)
tmp = tmp[:-2] + ">"
print(tmp)