N = int(input())
# INF = int(1e9)

T = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

dp = [-1] * N

dp[0] = C[0]

for i in range(1, N):
    dp[i] = max(C[i], dp[i - 1])

    target = T[i] - B[i]

    left = 0
    right = i - 1

    while left <= right:
        mid = (left + right) // 2

        curr = T[mid]

        if curr < target:
            left = mid + 1
        else:
            right = mid - 1

    while T[left] >= target and left >= 0:
        left -= 1

    if left < 0:
        continue

    dp[i] = max(dp[i], dp[left] + C[i])

print(dp[N - 1])
