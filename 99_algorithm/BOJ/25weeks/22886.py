import sys

input = sys.stdin.readline

T = int(input())
INF = int(1e9)

for t in range(1, T + 1):
    x, y, s = input().split()
    x = int(x)
    y = int(y)

    dp = [[INF] * len(s) for _ in range(2)]

    # J가 들어올 수도 있는 경우(J, ?)
    if s[0] != 'C':
        dp[0][0] = 0

    # C가 들어올 수도 있는 경우(C, ?)
    if s[0] != 'J':
        dp[1][0] = 0

    for i in range(1, len(s)):
        c = dp[1][i - 1]
        j = dp[0][i - 1]

        # J가 들어올 수도 있는 경우(J, ?) , CJ에 대한 비용(X) 지불
        if s[i] != 'C':
            dp[0][i] = min(dp[0][i - 1], c + x)

        # C가 들어올 수도 있는 경우(C, ?), JC에 대한 비용(Y) 지불
        if s[i] != 'J':
            dp[1][i] = min(dp[1][i - 1], j + y)

    print(f'Case #{t}: {min(dp[0][len(s) - 1], dp[1][len(s) - 1])}')
