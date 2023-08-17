#1,2,3 더하기 9095

##bottomUp
n = int(input())
params = list(int(input()) for _ in range(n))
maxParam = max(params)

dp = [0] * (maxParam + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, maxParam + 1):
  dp[i] = sum(dp[i-3:i])

for param in params:
  print(dp[param])

##topDown
def sol(num):
  if num == 1:
    return 1
  elif num == 2:
    return 2
  elif num == 3:
    return 4
  else:
    arr[num] = sol(num-1) + sol(num-2) + sol(num-3)
    return arr[num]

n = int(input())
params = list(int(input()) for _ in range(n))
maxParam = max(params)

arr = [0] * (maxParam + 1)
arr[1] = 1
arr[2] = 2
arr[3] = 4
sol(maxParam)

for param in params:
  print(arr[param])