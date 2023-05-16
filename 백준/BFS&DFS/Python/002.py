#미로탐색

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, " ".join(input()).split())))

#BFS
from collections import deque

cnt = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append([0,0])
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy
        nx = x + dx
        if (0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1):
            graph[ny][nx] += graph[y][x]
            q.append([ny, nx])

print(graph[n-1][m-1])
