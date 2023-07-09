#듣보잡 1764

n, m = map(int, input().split())

a = set()
for _ in range(n):
    a.add(input())
b = set()
for _ in range(n):
    b.add(input())

ans = sorted(list(a & b))
print(len(ans))
for i in ans:
    print(i)