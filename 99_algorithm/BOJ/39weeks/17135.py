import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def reset():
    for i in range(N):
        for j in range(M):
            if A[i][j] == 2:
                A[i][j] = 1


def solve(a, b, c):
    rst = 0
    for i in range(N - 1, -1, -1):

        die = set()
        for j in [a, b, c]:
            queue = deque()
            queue.append((i, j, 1))
            visited = [[False] * M for _ in range(N)]
            visited[i][j] = True
            while queue:
                row, col, dist = queue.popleft()
                if A[row][col] == 1:
                    die.add((row, col))
                    break

                if dist == D:
                    continue

                for k in range(3):
                    nx, ny = row + dx[k], col + dy[k]

                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))

        for (rr, cc) in die:
            rst += 1
            A[rr][cc] = 2

    return rst


dx = [0, -1, 0]
dy = [-1, 0, 1]

N, M, D = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for (x, y, z) in combinations(list(range(M)), 3):
    ans = max(ans, solve(x, y, z))
    reset()

print(ans)
