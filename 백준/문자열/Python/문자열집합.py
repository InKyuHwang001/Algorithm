#문자열 집합 14425

##set
n, m = map(int, input().split())
s = set()
for _ in range(n):
  s.add(input())

cnt = 0
for _ in range(m):
  tmp = input()
  if tmp in s:
    cnt += 1
print(cnt)

##dict
n, m = map(int, input().split())
d = {}
cnt = 0

for _ in range(n):
  d[input()] = True

for _ in range(m):
  if input() in d:
    cnt += 1

print(cnt)