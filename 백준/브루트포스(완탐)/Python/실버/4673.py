# 셀프넘버: 4673

## 리스트
numbers = list(range(1, 10_001))
notSelfNum = []
for num in numbers:
  tmp = num
  for n in str(num):
    tmp += int(n)
  if tmp <= 10_000:
    notSelfNum.append(tmp)
for rn in set(notSelfNum):
  numbers.remove(rn)

for i in numbers:
  print(i)

## set
numbers = set(range(1, 10_001))
notSelfNum = set()
for num in numbers:
  tmp = num
  for n in str(num):
    tmp += int(n)
  if tmp <= 10_000:
    notSelfNum.add(tmp)

numbers = numbers - notSelfNum
for selfNum in sorted(numbers):
  print(selfNum) 

## 함수화
def d(n):
  return n + sum(map(int, str(n)))

notSelfNum = set()
for i in range(1, 10_001):
  notSelfNum.add(d(i))

for j in range(1, 10_001):
  if j not in notSelfNum:
    print(j)