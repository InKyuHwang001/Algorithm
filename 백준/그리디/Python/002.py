#잃어버린 괄호

## -뒤에 수가 -가 오기전까지 더하여 맨 앞수에 뺌

a = input().split('-')

num = []

for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)