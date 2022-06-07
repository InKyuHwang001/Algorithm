# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 12:42:37 2022

@author: nadai
"""
# 미로 탐색
# https://www.acmicpc.net/problem/2178
'''
1.아이디어
0,0에서 시작 가면서 +1 후 값비교 표시
마지막 출력
2.
3.
지도 int[][]
chk int[][]
'''

from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = [stdin.readline().rstrip() for _ in range(N)]
# 방문경로 배열
visited = [[0]*M for _ in range(N)]
# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
#---------------------------------------------
# 단지번호붙이기
# https://www.acmicpc.net/problem/2667
'''

'''
from collections import deque
N = int(input())
maps = [list(input()) for _ in range(N)]
done = []
total = 0
result = []

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    queue = deque()

    queue.append((x, y))
    maps[x][y] = '0'
    done.append((x, y))

    while queue:
        now = queue.popleft()
        cnt += 1

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if(0 <= nx < N) and (0 <= ny < N):
                if maps[nx][ny] == '1' and ((nx, ny) not in done):
                    maps[nx][ny] = '0'
                    queue.append((nx, ny))
                    done.append((nx, ny))
    return cnt

for i in range(N):
    for j in range(N):
        if maps[i][j] == '1':
            result.append(bfs(i, j))
            total += 1

result.sort()
print(total)
for i in range(total):
    print(result[i])
