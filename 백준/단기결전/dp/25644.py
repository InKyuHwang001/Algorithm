n = int(input())
arr = list(map(int, input().split()))

dp = [0]*(n)

minNum = arr[0]

for i in range(n):
  minNum = min(minNum, arr[i])
  dp[i]= arr[i] - minNum

print(max(dp))