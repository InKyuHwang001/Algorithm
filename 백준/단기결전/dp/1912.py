n = int(input())
A = list(map(int, input().split()))

dp = [0]*n
dp[0] = A[0]
for idx in range(1,n):
  dp[idx] = max(dp[idx-1], 0) + A[idx]
print(max(dp))

####
n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
  if dp[i-1] > 0:
    dp[i] += dp[i-1]
print(max(dp))