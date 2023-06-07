#체스판 다시 칠하기 : 1018

##1차
n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(input())

ans = list()
for i in range(n - 7):
  for j in range(m - 7):
    wStart = 0
    bStart = 0
    for y in range(i, i + 8):
      for x in range(j, j + 8):
        if (y + x) % 2 == 0:
          if board[y][x] == "B":
            wStart += 1
          else:
            bStart += 1
        else:
          if board[y][x] == "W":
            wStart += 1
          else:
            bStart += 1
    ans.append(wStart)
    ans.append(bStart)

print(min(ans))

##2차
n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(input())

color = {0:"B", 1:"W"}
ans = list()

for i in range(n - 7):
  for j in range(m - 7):
    wStart = 0
    bStart = 0
    for y in range(i, i + 8):
      for x in range(j, j + 8):
        if board[y][x] != color[(y+x)%2]:
          bStart += 1
        else:
          wStart += 1
    ans.append(min(wStart, bStart))

print(min(ans))