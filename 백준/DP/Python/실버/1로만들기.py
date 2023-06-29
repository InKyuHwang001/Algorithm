# 1로 만들기 1463

n = int(input())
dp = [0] * (n+1)

for i in range(2, n + 1):
  dp[i] = dp[i -1] + 1
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[n])  

#top-down
n = int(input())
dp = {1:0}

def sol(n):
  if (n%3==0) and (n%2==0):
    dp[n]=min(sol(n//3)+1, sol(n//2)+1)
  elif n%3==0:
    dp[n]=min(sol(n//3)+1, sol(n-1)+1)
  elif n%2==0:
    dp[n]=min(sol(n//2)+1, sol(n-1)+1)
  else:
    dp[n]=sol(n-1)+1
    return dp[n]
  
	if n in dp.keys():
    return dp[n]
  
print(sol(n))

#bfs
from collections import deque
x=int(input())
Q=deque([x])
visited=[0]*(x+1)
while Q:
    c=Q.popleft()
    if c==1:
        break
    if c%3==0 and visited[c//3]==0:
        Q.append(c//3)
        visited[c//3]=visited[c]+1
    if c%2==0 and visited[c//2]==0:
        Q.append(c//2)
        visited[c//2]=visited[c]+1
    if visited[c-1]==0:
        Q.append(c-1)
        visited[c-1]=visited[c]+1
print(visited[1])