#14888 연산자 끼워넣기

def sol(idx,res):
    global minAns, maxAns
    
    if idx==N-1:
        minAns = min(minAns, res)
        maxAns = max(maxAns, res)
        return 
    
    for i in range(4):
        temp = res
        if operator[i]==0:
            continue
        if i == 0:
            res += numArr[idx+1]
        elif i == 1:
            res -= numArr[idx+1]
        elif i == 2:
            res *= numArr[idx+1]
        else:
            if res < 0:
                res = abs(res) // numArr[idx+1] * -1
            else:
                res //= numArr[idx+1]
        operator[i] -= 1
        sol(idx+1,res)
        operator[i] += 1
        res = temp

N = int(input())

numArr = list(map(int,input().split()))
operator = list(map(int,input().split()))

minAns = float('Inf')
maxAns = float('-Inf')

sol(0,numArr[0])
print(maxAns)
print(minAns)