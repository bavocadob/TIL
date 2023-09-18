import sys

sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, depth, s):
    if depth == 6:
        ans.add(s)
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, depth + 1, s + arr[nx][ny])


T = int(input())

for tc in range(T):
    arr = [list(input().split()) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, arr[i][j])

    print(f'#{tc + 1} {len(ans)}')
