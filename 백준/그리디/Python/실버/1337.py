
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
ans = [] 
for num in nums:
  cnt = 4
  tmps = [x+num for x in range(1, 5)]
  for tmp in tmps:
      if tmp in nums:
        cnt -= 1
  ans.append(cnt)
print(min(ans))

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
ans = [] 
for i in range(n):
  cnt = 0
  for j in range(nums[i], nums[i]+5):
      if j not in nums:
        cnt += 1
  ans.append(cnt)
print(min(ans))
