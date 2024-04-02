T = int(input())
for _ in range(T):

  N = int(input()) #동전가지수
  coins = list(map(int, input().split()))
  M = int(input()) #목표

  dp = [0] * (M + 1)
  dp[0] = 1
  for coin in coins:
    for money in range(M+1):
      if money >= coin:
        dp[money] += dp[money - coin]
