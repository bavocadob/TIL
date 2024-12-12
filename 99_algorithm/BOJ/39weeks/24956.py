N = int(input())
MOD = 1_000_000_007
A = input().rstrip()
ans = 0

dp = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(3):
        dp[i][j] = dp[i - 1][j]

    char = A[i - 1]

    if char == 'W':
        dp[i][0] += 1
    elif char == 'H':
        dp[i][1] += dp[i - 1][0]
    elif char == 'E':
        ans *= 2
        dp[i][2] += dp[i - 1][1]
        ans += dp[i - 1][2]

    ans %= MOD

print(ans)
