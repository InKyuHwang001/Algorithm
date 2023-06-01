from collections import deque


n =  int(input())
m =  int(input())

arr = [[0]*n for _  in range(n)]
visited = [False]*n

for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

#DFS
cnt = 0
def dfs(x):
    global cnt
    visited[x] = True
    for i in range(n):     
        if (arr[i][x] == 1) and (visited[i] == False):    
            cnt += 1
            dfs(i)
dfs(0)
print(cnt)

#BFS
cnt = 0
q = deque()
q.append(0)
visited[0]= True

while q:
    now = q.popleft()
    for i in range(n):
        if arr[now][i]==1 and visited[i]==False:
            visited[i]=True
            q.append(i)
            cnt+=1
print(cnt)