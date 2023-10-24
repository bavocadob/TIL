import sys

input = sys.stdin.readline
N = int(input())
ans = 0

lines = list()
for _ in range(N):
    x, y = map(int, input().split())
    lines.append((x, y))

# lines.sort(key=lambda x: x[1])
lines.sort()
left = -int(1e10)
right = -int(1e10)
for x, y in lines:
    if x > right:
        ans += right - left
        left, right = x, y
    elif x <= right < y:
        right = y

ans += right - left

print(ans)
