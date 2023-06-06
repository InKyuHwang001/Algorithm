#덩치: 7568 

"""
솔팅 후 값을모 인덱싱 하여 출려고 했으나 이는 좋흔 방법이 아닌거 같아

자신보다 큰 수가 몇게인지 찾는 방법으로 바꿈
"""


n = int(input())
peoples = []
for _ in range(n):
  peoples.append(list(map(int, input().split())))
ans = [1] * n

for i in range(len(peoples)):
  weight, height = peoples[i]
  for other in peoples:
    otherWeight, otherHeight = other
    if otherWeight > weight and otherHeight > height:
      ans[i] += 1
for rank in ans:
  print(rank, end=' ')

## ans list없이 풀기
n = int(input())
peoples = []
for _ in range(n):
  peoples.append(list(map(int, input().split())))
for people in peoples:
  rank = 1
  for other in peoples:
    if people[0] < other[0] and people[1] < other[1]:
      rank += 1
  print(rank, end=' ')

## 1번을 효율화
n = int(input())
peoples = []
for _ in range(n):
  peoples.append(list(map(int, input().split())))
ans = [1] * n

for i in range(len(peoples)):
  weight, height = peoples[i]
  for j in range(i+1, len(peoples)):
    otherWeight, otherHeight = peoples[j]
    if otherWeight > weight and otherHeight > height:
      ans[i] += 1
    elif otherWeight < weight and otherHeight < height:
      ans[j] +=1
for rank in ans:
  print(rank, end=' ')

##딕셔너리로 푼 다른사람 출이
import sys

num_of_giant = int(sys.stdin.readline())

giant_list = []

for _ in range(num_of_giant):
    input_value = list(map(int, sys.stdin.readline().split()))
    giant = {'weight': input_value[0], 'height': input_value[1]}
    giant_list.append(giant)

for i in giant_list:
    ranking = 1
    for j in giant_list:
        if i['weight'] < j['weight'] and i['height'] < j['height']:
            ranking += 1

    print(ranking, end=" ")