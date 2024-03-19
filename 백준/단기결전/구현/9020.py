def sol(num):
  for n in range(2, int(num**(1/2)+1)):
    if num%n ==0:
      return False
  return True

for _ in range(int(input())):
  n = int(input())
  
  s, e = n//2, n//2
  while s>0:
    if sol(s) and sol(e):
      break
    else:
      s -= 1
      e += 1
  print(s, e)

def check(n):
  if n == 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

T = int(input())
for _ in range(T):
  n = int(input())
  s, e = n//2, n//2

  while True:
    if check(s) and check(e):
      print(s, e)
      break
    else:
      s -= 1
      e += 1