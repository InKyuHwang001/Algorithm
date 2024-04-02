import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))

m = int(input())
ans = list(map(int, input().split()))

dic = {x:0 for x in ans}

for card in cards:
  if card in dic:
    dic[card] += 1
a = []
for num in ans:
  a.append(dic[num])
print(*a)