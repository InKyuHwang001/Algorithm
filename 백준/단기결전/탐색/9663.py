# 2차원은 1차원으로 축소하여 표현이 가능하다.


n = int(input())

ans = 0
row = [-1] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)
            row[x] = -1
n_queens(0)
print(ans)

###################################

from itertools import permutations
N = int(input())

candidates =list(permutations(range(8)))
def check(arr):
  alen = len(arr)
  for i in range(alen):
    for j in range(i+1,alen):
      if abs(arr[i] - arr[j]) ==  abs(i-j):
        return False
  return True
ans = 0
for candi in candidates:
  if check(candi):
    ans+=1
print(ans)