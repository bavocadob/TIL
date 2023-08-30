import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def valid(x, y):
    return 0 <= x < N and 0 <= y < M


def bfs(queue, left, right):
    ans = 0
    while left < right:
        x, y = queue[left]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if valid(nx, ny) and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                ans += visited[nx][ny]
                queue.append((nx, ny))
                right += 1

        left += 1

    return ans


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    visited = [[-1] * M for _ in range(N)]
    queue = []
    field = []
    queue_size = 0
    for i in range(N):
        f = input().rstrip()
        for j in range(M):
            if f[j] == 'W':
                visited[i][j] = 0
                queue.append((i, j))
                queue_size += 1
        field.append(f)

    print(f'#{tc + 1} {bfs(queue, 0, queue_size)}')
