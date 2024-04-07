N = int(input())

def makeStar(sy, sx, length):
  #3으로 나누어진 값
  length = length//3
  
  for ny in range(sy + length, sy + 2*length):
    for nx in range(sx + length, sx + 2*length):
      graph[ny][nx] = " "
  if length >=3:
    makeStar(sy, sx, length)
    
    makeStar(sy+length, sx, length)
    makeStar(sy+2*length, sx, length)

    makeStar(sy, sx+length, length)
    makeStar(sy, sx+2*length, length)

    makeStar(sy+length, sx+2*length, length)
    makeStar(sy+2*length, sx+2*length, length)
    makeStar(sy+2*length, sx+length, length)

graph = [["*" for _ in range(N)] for _ in range(N)]

makeStar(0,0, N)
for li in graph:
  for l in li:
    print(l, end="")
  print()


## 코드 개선
N = int(input())

def makeStar(sy, sx, length):
  length = length//3
  
  for ny in range(sy + length, sy + 2*length):
    for nx in range(sx + length, sx + 2*length):
      graph[ny][nx] = " "
      
  if length >=3:
    for dy in range(3):
      for dx in range(3):
        if dy == 1 and dx == 1:
          continue
        makeStar(sy + dy * length, sx + dx * length, length)

graph = [["*" for _ in range(N)] for _ in range(N)]

makeStar(0,0, N)
for li in graph:
  print("".join(li))