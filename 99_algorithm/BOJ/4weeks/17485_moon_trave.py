N, M = map(int, input().split())

cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * M for _ in range(N)] for _ in range(3)]


print(dp[0])

