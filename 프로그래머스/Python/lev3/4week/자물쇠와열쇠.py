def keyShift(key, idx, m):
    if idx == 0:
        return key
    tmp = [[0]*m for _ in range(m)]
    if idx == 1:
        for y in range(m):
            for x in range(m):
                tmp[x][m-1-y] = key[y][x]
        
    elif idx == 2:
        for y in range(m):
            for x in range(m):
                tmp[y][x] = key[m-1-y][m-1-x]
    else:
        for y in range(m):
            for x in range(m):
                tmp[m-1-x][y] = key[y][x]
    return tmp

def chek(nlock,n):
    for y in range(n, 2*n):
        for x in range(n, 2*n):
            if nlock[y][x] != 1:
                return False
    return True
def solution(key, lock):
    n = len(lock) #lock
    m = len(key)
    nlock = [[0] * (3*n) for _ in range(3 *n)]
    
    for y in range(n):
        for x in range(n):
            nlock[n+y][n+x] = lock[y][x]
    
    for y in range(1, 2*n):
        for x in range(1, 2*n):
            for idx in range(4):
                mkey = keyShift(key, idx, m)
                for keyy in range(m): 
                    for keyx in range(m):
                        nlock[y+keyy][x+keyx] += mkey[keyy][keyx]
                if chek(nlock,n):
                    return True
                for keyy in range(m): 
                    for keyx in range(m):
                        nlock[y+keyy][x+keyx] -= mkey[keyy][keyx]
    return False