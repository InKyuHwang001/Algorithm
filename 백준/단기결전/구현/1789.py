S = int(input())

ans = 0
while True:
  ans += 1
  if (ans+2) * (ans+1) / 2 >S:
    break
print(ans)

##############################
s = int(input())

total = 0
num = 0

while total <= s:
  num += 1
  total += num
print(num-1)