import heapq
X = int(input())
sticks = []
heapq.heappush(sticks, 64)
while sum(sticks) > X:
  shortest = heapq.heappop(sticks)
  stick = shortest/2
  if stick + sum(sticks) < X:
    heapq.heappush(sticks, stick)
  heapq.heappush(sticks, stick)

print(len(sticks))

################################
x = int(input())

makdes = [64]

while sum(makdes) != x:
  tmp = makdes.pop()//2
  makdes.append(tmp)
  if sum(makdes) < x:
    makdes.append(tmp)
print(len(makdes))