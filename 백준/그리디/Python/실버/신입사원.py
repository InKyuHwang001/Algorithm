#신입 사원 1946

t = int(input())

for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort(key = lambda x : x[0])

    cnt = 1
    min = lst[0][1]

    for i in range(1, n):
        if lst[i][1] < min:
            min = lst[i][1]
            cnt += 1
            
    print(cnt)