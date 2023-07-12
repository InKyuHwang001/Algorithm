#그룹 단어 체커 1316
##
n = int(input())
ans = 0
for _ in range(n):
  strings = input()
  tmp = []
  for i in range(len(strings)):
    if i < 1 :
      tmp.append(strings[i])
    elif tmp[-1] != strings[i]:
      tmp.append(strings[i])
  if len(tmp) == len(set(tmp)):
    ans += 1
print(ans)

##
n = int(input())
ans = 0

for _ in range(n):
  word = input()
  error = True
  for i in range(len(word) - 1):
    if word[i] != word[i+1]:
      new_word = word[i+1:]
      if new_word.count(word[i]) > 0:
        error = False
        break
  if error:
    ans += 1

print(ans)

##
n = int(input())
cnt = n

for _ in range(n):
  word = input()
  for i in range(len(word)-1):
    if word[i] == word[i+1]:
      pass
    elif word[i] in word[i+1:]:
      cnt-=1
      break
print(cnt)