#단어 정렬 1181

n = int(input())
ar = [input() for _ in range(n)]
ar = list(set(ar))
ar.sort(key = lambda x: (len(x), x))

for a in ar:
  print(a)