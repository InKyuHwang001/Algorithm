# 회의실 배정 1931
## 가장 빨리 끝나는 강의를 뽑자
N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

# time = sorted(time, key=lambda a: a[0]) 
# time = sorted(time, key=lambda a: a[1]) 
time.sort(key = lambda x: (x[1], x[0]))

last = 0 
conut = 0 

for i, j in time:
  if i >= last: 
    conut += 1
    last = j

print(conut)

# sorted(students, key=lambda student: (student[2], student[1]), reverse=True)
# [('홍길동', 3.9, 2016303), ('김철수', 3.0, 2016302), ('최자영', 4.3, 2016301)]