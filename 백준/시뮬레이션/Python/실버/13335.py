# 13335 트럭

##차를 빼내고 올리기를 반복한다.
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0]*w
cnt = 0

while bridge:
  cnt += 1
  bridge.pop(0)

  if trucks:
    if sum(bridge) + trucks[0] > l:
      bridge.append(0)
    else:
      bridge.append(trucks.pop(0))
print(cnt) 

#첫 코드에 다리 무게 계산이 중복임 -> 수정
##92ms -> 48ms
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0]*w
cnt = 0
weight = 0

while bridge:
  cnt += 1
  weight -= bridge.pop(0)

  if trucks:
    if weight + trucks[0] > l:
      bridge.append(0)
    else:
      tmp = trucks.pop(0)
      bridge.append(tmp)
      weight += tmp
print(cnt)