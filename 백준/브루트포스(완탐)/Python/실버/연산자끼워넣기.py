#연산자 끼워넣기 14888
n = int(input())
num = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

mymax = int(-1e9)
mymin = int(1e9)

def dfs(index, result, plus, minus, mul, div):
    global mymax, mymin
    if index == n:
        mymax = max(mymax, result)
        mymin = min(mymin, result)
        return
    if plus > 0 :
        dfs(index + 1, result + num[index], plus-1, minus, mul, div)
    if minus > 0 :
        dfs(index + 1, result - num[index], plus, minus-1, mul, div)
    if mul > 0:
        dfs(index + 1, result * num[index], plus, minus, mul-1, div)
    if div > 0 :
        dfs(index + 1, int(result / num[index]), plus, minus, mul, div-1)


dfs(1, num[0], plus, minus, mul, div)
print(mymax)
print(mymin)

##바꿈
n = int(input())
number = list(map(int, input().split()))
op = list(map(int, input().split()))
minR = int(1e9)
maxR = -int(1e9)

answer = number[0]

def dfs(idx):
    global answer
    global minR, maxR

    if idx == n:
        if answer > maxR:
            maxR = answer
        if answer < minR:
            minR = answer
        return

    for i in range(4):
        tmp = answer
        if op[i] > 0:
            if i == 0:
                answer += number[idx]
            elif i == 1:
                answer -= number[idx]
            elif i == 2:
                answer *= number[idx]
            else:
                if answer >= 0:
                    answer //= number[idx]
                else:
                    answer = (-answer // number[idx]) * -1

            op[i] -= 1
            dfs(idx+1)
            answer = tmp
            op[i] += 1


dfs(1)
print(maxR)
print(minR)