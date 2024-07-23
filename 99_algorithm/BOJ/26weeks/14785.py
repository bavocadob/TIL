import sys

input = sys.stdin.readline
N = int(input())

A = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append((a, a + b))

A.sort()

cur = -1
ans = 0

for start, end in A:
    if start >= cur:
        ans += 1
        cur = end
    else:
        cur = min(end, cur)

print(ans)
