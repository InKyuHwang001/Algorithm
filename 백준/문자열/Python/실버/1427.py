#1427 소트인사이드
##
arr = list(input())
arr.sort(reverse=True)
tmp = ''
for a in arr:
  tmp += a
print(tmp)

##
li = list(map(int, input()))
li.sort(reverse=True)

for i in li:
    print(i,end='')