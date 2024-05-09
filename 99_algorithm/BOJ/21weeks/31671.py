import sys

sys.setrecursionlimit(999999)
input = sys.stdin.readline


def is_valid(x, y):
    if x <= N:
        y_max = x
    else:
        x -= N
        y_max = N - x

    if y < 0 or y > y_max:
        return False

    return True


dx = [1, 1]
dy = [-1, 1]


def solve(x, y):
    if dp[x][y] != -2:
        return dp[x][y]

    temp = -2
    for k in range(2):
        nx, ny = x + dx[k], y + dy[k]

        if not is_valid(nx, ny):
            continue

        if (nx, ny) in teachers:
            continue

        temp = max(temp, solve(nx, ny))

    if temp == -2 or temp == -1:
        dp[x][y] = -1
    else:
        dp[x][y] = max(temp, y)

    return dp[x][y]


N, M = map(int, input().split())

teachers = set()

for _ in range(M):
    teachers.add(tuple(map(int, input().split())))

dp = [[-2] * (N + 1) for _ in range(N * 2 + 1)]
dp[N * 2][0] = 0

print(solve(0, 0))
