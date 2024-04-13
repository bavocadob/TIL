INF = float('inf')
N = int(input())

A = [0] + list(map(int, input().split()))

dp = [[INF] * (N + 1) for _ in range(N + 1)]

dp[0][1] = 0
dp[1][0] = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        k = max(i, j) + 1
        A[0] = A[k]
        dp[i][k] = min(dp[i][k], dp[i][j] + abs(A[k] - A[j]))
        dp[k][j] = min(dp[k][j], dp[i][j] + abs(A[k] - A[i]))

ans = INF

for i in range(N):
    ans = min(ans, dp[i][N], dp[N][i])

print(ans)
