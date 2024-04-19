def f(x, y, w):
    h1 = (x**2-w**2)**0.5
    h2 = (y**2-w**2)**0.5    
    c = h1*h2 / (h1+h2)
    return c
x, y, c = map(float, input().split())

s, e = 0, min(x,y)

while e - s > 0.000001:
  m = (s+e)/2

  tmp = f(x, y, m)
  if tmp >= c:
    s = m
  else:
    e = m
print(s)