#1417 국회의원 선거

n = int(input())
da = int(input())
votes = []
for _ in range(n-1):
  votes.append(int(input()))
cnt = 0

votes.sort(reverse = True)

if n == 1:
  print(0)
else:
  while votes[0] >= da:
    da+=1
    votes[0] -= 1
    cnt += 1
    votes.sort(reverse=True)
  print(cnt)


##
n = int(input())
da = int(input())
if n <= 1 :
  print(0)
else :
  others = []
  for _ in range(n-1) :
    others.append(int(input()))

  cnt = 0
  while max(others) >= da :
    data = others.index(max(others))
    da += 1
    others[data] -=1
    cnt += 1

  print(cnt)