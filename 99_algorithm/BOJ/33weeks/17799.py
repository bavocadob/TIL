import sys

input = sys.stdin.readline
N, C = map(int, input().split())

A = sorted(list(map(int, input().split())))
ans = 0

left = 0
right = N - 1

while left < right:
    temp = A[left] + A[right]

    if temp <= C:
        left += 1
        right -= 1
        ans += 1
        continue

    right -= 1
    ans += 1

if left == right:
    ans += 1

print(ans)
