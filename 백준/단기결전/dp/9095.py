T = int(input())
ar = [int(input()) for _ in range(T)]

dp = [0]*(max(ar)+1)

dp[1] = 1 #1
dp[2] = 2 #1+1, 2
dp[3] = 4 #1+1+1 2+1 1+2 3

lenDp = len(dp)

for idx in range(4, lenDp):
  dp[idx] = dp[idx -1] + dp[idx -2] + dp[idx -3]

for a in ar:
  print(dp[a])