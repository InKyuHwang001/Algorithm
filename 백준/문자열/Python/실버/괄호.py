#괄호 9012

n = int(input())

for k in range(n):
  ps = input()
  tmp = 0
  maxp = len(ps)
  for i in range(maxp):
    if tmp < 0:
      print("NO")
      break

    if ps[i] == '(':
        tmp += 1
    else:
      tmp -= 1

    if i == maxp - 1:
      if tmp == 0:
        print("YES")
      else:
        print("NO") 



## 효율성 업글
n = int(input())

for _ in range(n):
    line = input()
    stack = []

    for i in line:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')