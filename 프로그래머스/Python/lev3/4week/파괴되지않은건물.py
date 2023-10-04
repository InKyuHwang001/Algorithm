ATTACK = 1
HILL = 2

def solution(board, skill):
    update(board, skill)
    answer = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if is_not_destroyed(board,y,x):
                answer+=1
    return answer

def is_not_destroyed(board,y,x):
    return board[y][x] > 0

def update(board, skill):
    diff = [[0]*(len(board[0])+1) for _ in range(len(board) +1)]
    for type, r1,c1,r2,c2, degree in skill:
        d = -degree if type == ATTACK else degree
        diff[r1][c1] += d
        diff[r1][c2 + 1] -= d
        diff[r2+1][c1] -= d
        diff[r2+1][c2+1] += d
    for y in range(len(board)):
        for x in range(1, len(board[0])):
            diff[y][x]+= diff[y][x-1]
    for x in range(len(board)):
        for y in range(1, len(board[0])):
            diff[y][x]+= diff[y-1][x]
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x]+= diff[y][x]