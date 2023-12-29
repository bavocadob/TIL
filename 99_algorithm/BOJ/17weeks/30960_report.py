N = int(input())

A = list(map(int, input().split()))
A.sort()

dp = [0] * N

dp[1] = A[1] - A[0]
dp[2] = A[2] - A[0]

for i in range(3, N):
    if i % 2:
        dp[i] = dp[i - 2] + (A[i] - A[i - 1])
    else:
        dp[i] = min(dp[i - 2] + A[i] - A[i - 1], dp[i - 3] + A[i] - A[i - 2])

print(dp[N - 1])
