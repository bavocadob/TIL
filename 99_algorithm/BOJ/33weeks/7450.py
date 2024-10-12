import sys

input = sys.stdin.readline
N = int(input())

L = int(input())

A = [int(input()) for _ in range(N)]

A.sort()
ans = 0

left = 0
right = N - 1

while left <= right:
    temp = A[left] + A[right]
    if temp <= L:
        ans += 1
        left += 1
        right -= 1
    else:
        right -= 1
        ans += 1

print(ans)
