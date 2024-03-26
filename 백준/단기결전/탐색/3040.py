from itertools import combinations
peoples = [int(input())for _ in range(9)]


indexes = list(combinations(peoples, 7))
for index in indexes:
  if sum(index) == 100:
    for people in index:
      print(people)
    