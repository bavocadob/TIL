import sys

input = sys.stdin.readline
N = int(input())

nums = list(map(int, input().split()))

dp_plus = [0] * N
dp_minus = [0] * N

dp_plus[0] = 1
dp_minus[N - 1] = 1

for i in range(1, N):
    dp_plus[i] = 1
    for j in range(i):
        if nums[i] > nums[j]:
            dp_plus[i] = max(dp_plus[i], dp_plus[j] + 1)

for i in range(N - 2, -1, -1):
    dp_minus[i] = 1
    for j in range(i + 1, N):
        if nums[i] > nums[j]:
            dp_minus[i] = max(dp_minus[i], dp_minus[j] + 1)

ans = 0
for i in range(N):
    ans = max(ans, dp_plus[i] + dp_minus[i] - 1)

print(ans)
