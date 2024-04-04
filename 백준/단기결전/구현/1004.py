import sys
input = sys.stdin.readline

def is_in(x, y, astro):
  cx, cy, r = astro
  if ((y- cy)**2 + (x- cx)**2)**0.5 > r:
    return False
  return True

T = int(input())
for _ in range(T):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())


  astros = [list(map(int, input().split())) for _ in range(n)]
  ans = 0
  for astro in astros:
    #1이 안에있냐
    TF1 = is_in(x1, y1, astro) 

    TF2 = is_in(x2, y2, astro) 
    if TF1 != TF2:
      ans+=1
  print(ans)