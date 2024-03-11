
N = int(input())
M = int(input())
nums = list(map(int, input().split()))

s, e = nums[0], (N - nums[-1])

mid = 0
for i in range(1, len(nums)):
  mid = max(mid, (nums[i] - nums[i-1]+1)/2)

print(max(s, e, mid))

#성능 개선버전
def bs(li, m):
    if li[1]-li[0] > m:
        return 0
    if li[-1]-li[-2] > m:
        return 0
    for i in range(1, len(li)-2):
        if (li[i+1]-li[i])/2 > m:
            return 0
    return 1

N, M = int(input()), int(input())
li = [0] + list(map(int, input().split())) + [N]
s, e = 0, N
res = 0
while s <= e:
    m = (s+e)//2
    if bs(li, m):
        e = m-1
        res = m
    else:
        s = m+1
print(res)