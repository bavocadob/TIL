N = int(input())
INF = int(1e9)
dp = [-INF] * (N + 1)
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rst = 0

for i in range(N):
    if B[i]:
        rst += A[i]
        dp[i + 1] = max(-A[i], dp[i] - A[i])
    else:
        dp[i + 1] = max(A[i], dp[i] + A[i])


print(rst + max(dp))