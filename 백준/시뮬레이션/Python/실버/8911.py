#8911 거북이
from collections import deque
dy = [1,0,-1,0] #북 동 남 서
dx = [0,1,0,-1]
n = int(input())

for _ in range(n):
  commands = deque(list(' '.join(input()).split()))
  h = [0]
  w = [0]
  dir = 0
  x, y = 0, 0
  while commands:
    com = commands.popleft()
    if com == "F":
      x += dx[dir]
      y += dy[dir]
    elif com == "B":
      x -= dx[dir]
      y -= dy[dir]
    elif com =="R":
      dir = int((dir + 1)%4)
    else:
      dir = int((dir - 1)%4)
    h.append(y)
    w.append(x)
  ansh = abs(max(h) - min(h))
  answ = abs(max(w) - min(w))
  print(ansh*answ)