#주유소 13305
## 뒤의 마지맋 수는 무시한다. 
## 가장 작은 수를 기준으로 나누어 간다.

n = int(input())

dis = list(map(int, input().split()))
price = list(map(int, input().split()))

minPrice = price[0]
ans = 0

for i in range(n-1):
    if minPrice > price[i]:
        minPrice = price[i]
    ans += minPrice * dis[i]

print(ans)