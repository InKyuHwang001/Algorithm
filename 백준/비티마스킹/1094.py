x = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(stick)):
    if x >= stick[i]:
        count += 1
        x -= stick[i]

    if x == 0:
        break

print(count)



x = int(input())

makdes = [64]

while sum(makdes) != x:
  tmp = makdes.pop()//2
  makdes.append(tmp)
  if sum(makdes) < x:
    makdes.append(tmp)
print(len(makdes))