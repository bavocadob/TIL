N = int(input())

S = input().rstrip()

dp = [[0] * (N + 1) for _ in range(3)]

ans = 0

for i in range(N):
    for j in range(3):
        dp[j][i] = dp[j][i - 1]

    if S[i] == 'D':
        dp[0][i] += 1
    elif S[i] == 'K':
        dp[1][i] += dp[0][i - 1]
    elif S[i] == 'S':
        dp[2][i] += dp[1][i - 1]
    elif S[i] == 'H':
        ans += dp[2][i - 1]

print(ans)
