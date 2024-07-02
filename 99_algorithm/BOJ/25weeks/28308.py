import sys

input = sys.stdin.readline

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def dfs(x, y, word_idx, direction, curved):
    global ans
    if word_idx == len(word):
        ans += 1
        return

    for k in range(-2, 3, 2):
        next_direction = (direction + k) % 8
        nx, ny = x + dx[next_direction], y + dy[next_direction]
        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if A[nx][ny] == word[word_idx]:
            if k == 0:
                dfs(nx, ny, word_idx + 1, next_direction, curved)
            elif k != 0 and curved and word_idx > 1:
                dfs(nx, ny, word_idx + 1, next_direction, False)


word = input().rstrip()
N = int(input())

M = int(input())

ans = 0

A = [list(input().rstrip().split()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if A[i][j] == word[0]:
            for kk in range(8):
                dfs(i, j, 1, kk, True)

print(ans)
