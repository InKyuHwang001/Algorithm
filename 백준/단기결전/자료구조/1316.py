N = int(input())
words = [input() for _ in range(N)]
ans = 0
for word in words:
  tf = True
  tmp = []
  for st in word:
    if st not in tmp:
      tmp.append(st)
    
    else:
      if st != tmp[-1]:
        tf = False
        break
  if tf == True:
    ans += 1 
print(ans)