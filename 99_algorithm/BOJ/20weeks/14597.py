def get_area(x):
    return x * x


def solve(x, y):
    if x == N:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = solve(x + 1, y)
    if y != 0:
        dp[x][y] = min(dp[x][y], solve(x + 1, y - 1))
    if y != M - 1:
        dp[x][y] = min(dp[x][y], solve(x + 1, y + 1))
    dp[x][y] += get_area(abs(A[x][y] - B[x][y]))
    return dp[x][y]


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]

ans = int(1e9)
for i in range(M):
    ans = min(ans, solve(0, i))

print(ans)
