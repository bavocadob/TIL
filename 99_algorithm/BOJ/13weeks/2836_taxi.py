import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ans = M

customer = []

for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        customer.append((a, b))

customer.sort(key=lambda x: x[1])

left = 0
right = 0

for l, r in customer:
    if r > left:
        ans += (left - right) * 2
        left = l
        right = r
    else:
        left = max(left, l)
        right = min(right, r)

ans += (left - right) * 2

print(ans)
