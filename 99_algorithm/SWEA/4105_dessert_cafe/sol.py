# 왼쪽 아래 -> 오른쪽 아래 -> 오른쪽 위 -> 왼쪽 위 순서
import sys

sys.stdin = open('input.txt')

dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]


def valid_range(x, y):
    return 0 <= x < N and 0 <= y < N


def dfs(depth, x, y):
    global result

    if depth == 3 and distance[depth] == distance[depth - 2]:
        if result < sum(visited):
            result = sum(visited)
        return

    if depth < 2:
        nx, ny = x + dx[depth], y + dy[depth]
        if valid_range(nx, ny) and not visited[cafe[nx][ny]]:
            visited[cafe[nx][ny]] = True
            distance[depth] += 1
            dfs(depth, nx, ny)
            visited[cafe[nx][ny]] = False
            distance[depth] -= 1

        if distance[depth] > 0:
            nx, ny = x + dx[depth + 1], y + dy[depth + 1]
            if valid_range(nx, ny) and not visited[cafe[nx][ny]]:
                visited[cafe[nx][ny]] = True
                distance[depth + 1] += 1
                dfs(depth + 1, nx, ny)
                visited[cafe[nx][ny]] = False
                distance[depth + 1] -= 1
    elif depth >= 2:
        if distance[depth] < distance[depth - 2]:
            nx, ny = x + dx[depth], y + dy[depth]
            if valid_range(nx, ny) and not visited[cafe[nx][ny]]:
                visited[cafe[nx][ny]] = True
                distance[depth] += 1
                dfs(depth, nx, ny)
                visited[cafe[nx][ny]] = False
                distance[depth] -= 1
        elif distance[depth] == distance[depth - 2]:
            nx, ny = x + dx[depth + 1], y + dy[depth + 1]
            if valid_range(nx, ny) and not visited[cafe[nx][ny]]:
                visited[cafe[nx][ny]] = True
                distance[depth + 1] += 1
                dfs(depth + 1, nx, ny)
                visited[cafe[nx][ny]] = False
                distance[depth + 1] -= 1


T = int(input())

for tc in range(T):

    N = int(input())

    cafe = [list(map(int, input().split())) for _ in range(N)]
    distance = [0, 0, 0, 0]
    visited = [False] * 101

    result = -1

    for i in range(N):
        for j in range(N):
            # visited[cafe[i][j]] = True
            dfs(0, i, j)
            # visited[cafe[i][j]] = False

    print(f'#{tc + 1} {result}')
