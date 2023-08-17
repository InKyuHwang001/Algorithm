# 접미사 배열 11656

s = input()
slis = []
for i in range(len(s)):
  slis.append(s[i:])

slis.sort()

for sli in slis:
  print(sli)