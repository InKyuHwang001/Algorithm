S = list(" ".join(input()).split())

ar = []
ar.append(S[0])

for s in S:
  if s != ar[-1]:
    ar.append(s)

print(min(ar.count("0"), ar.count("1")))


S = input()
ans = 0
tmp = S[0]
length = len(S)
for i in range(1, length):
  if tmp != S[i] and S[i-1] != S[i]:
    ans += 1

print(ans)