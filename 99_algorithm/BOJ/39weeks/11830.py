from collections import defaultdict

x = []
y = []


N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

M = [defaultdict(int), defaultdict(int)]

for i in range(N):
    M[0][x[i]] += 1
    M[1][y[i]] += 1

ans = 0
for i in range(N):
    ans += (M[0][x[i]] - 1) * (M[1][y[i]] - 1)

print(ans)
