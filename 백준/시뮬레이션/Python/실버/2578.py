#2578 빙고

c = [list(map(int, input().split())) for _ in range(5)]
params = []
for _ in range(5):
    params += list(map(int, input().split()))


def check():
    tmp = 0

    for x in c: 
        if x.count(0) == 5:
            tmp += 1

    for i in range(5): 
        y = 0
        for j in range(5):
            if c[j][i] == 0:
                y += 1
        if y == 5:
            tmp += 1

    d1 = 0
    for i in range(5):
        if c[i][i] == 0:
            d1 += 1
    if d1 == 5:
        tmp += 1

    d2 = 0
    for i in range(5):
        if c[i][4-i] == 0:
            d2 += 1
    if d2 == 5:
        tmp += 1

    return tmp 


cnt = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if params[i] == c[x][y]:
                c[x][y] = 0
                cnt += 1

    if cnt >= 12:
        result = check()

        if result >= 3:
            print(i+1)
            break