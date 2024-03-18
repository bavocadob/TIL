N = int(input())


music = list(map(int, input().split()))

dp = [[0] * 5 for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(5):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + music[i - 1]
        elif j == 1 or j == 3:  # 겹친거  처리
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + music[i - 1] * 2
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + music[i - 1]

print(max(dp[N]))
