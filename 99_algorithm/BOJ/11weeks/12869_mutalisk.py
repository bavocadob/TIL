INF = int(1e9)


def solution(a, b, c):
    if dp[a][b][c] != -1:
        return dp[a][b][c]

    rst = INF

    if a:
        rst = min(rst, solution(max((a - 9), 0), max((b - 3), 0), max((c - 1), 0)))
        rst = min(rst, solution(max((a - 9), 0), max((b - 1), 0), max((c - 3), 0)))

    if b:
        rst = min(rst, solution(max((a - 3), 0), max((b - 9), 0), max((c - 1), 0)))
        rst = min(rst, solution(max((a - 1), 0), max((b - 9), 0), max((c - 3), 0)))
    if c:
        rst = min(rst, solution(max((a - 3), 0), max((b - 1), 0), max((c - 9), 0)))
        rst = min(rst, solution(max((a - 1), 0), max((b - 3), 0), max((c - 9), 0)))

    dp[a][b][c] = rst + 1
    return dp[a][b][c]


N = int(input())

hp = [0] * 3
scv_hp = list(map(int, input().split()))

dp = [[[-1] * 61 for _ in range(61)] for _ in range(61)]
dp[0][0][0] = 0

for i in range(N):
    hp[i] = scv_hp[i]

print(solution(*hp))
