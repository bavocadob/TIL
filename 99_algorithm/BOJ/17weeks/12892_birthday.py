import sys

input = sys.stdin.readline

N, D = map(int, input().split())

gift = list()

for _ in range(N):
    p, v = map(int, input().split())
    gift.append((p, v))

gift.sort()

left = right = 0

value = 0
ans = 0
while right < N:
    if gift[left][0] > gift[right][0] - D:
        value += gift[right][1]
        right += 1
        ans = max(value, ans)
    else:
        value -= gift[left][1]
        left += 1

print(ans)
