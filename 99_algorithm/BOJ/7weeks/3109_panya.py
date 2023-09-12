import sys

sys.setrecursionlimit(999999)
input = sys.stdin.readline


def dfs(row_index, col_index):
    pipe[row_index][col_index] = 'x'

    if col_index == M - 1:
        return 1

    for i in range(-1, 2):
        row = row_index + i

        if 0 <= row < N and pipe[row][col_index + 1] == '.':
            if dfs(row, col_index + 1):
                return 1
    return 0


N, M = map(int, input().split())

pipe = [list(input().rstrip()) for _ in range(N)]
ans = 0
for i in range(N):
    ans += dfs(i, 0)

print(ans)
