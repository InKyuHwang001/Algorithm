from itertools import product
for _ in range(int(input())):
  N = int(input())
  cal = [" ", "+", "-"]
  nums = list(range(1, N+1))

  for li in list(product(cal, repeat = N-1)):
    tmp = ""
    for idx in range(N-1):
      tmp += str(nums[idx])+ li[idx]
    tmp += str(nums[-1])
    if eval(tmp.replace(" ", "")) == 0:
      print(tmp)
  print()