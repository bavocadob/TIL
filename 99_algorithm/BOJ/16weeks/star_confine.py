# 우0 하1 좌2 상3
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution():
    result = []
    for i in range(N):
        x = i
        y = 0
        d = 0
        visited = [[[False] * M for _ in range(N)] for _ in range(4)]
        visited[d][x][y] = True
        flag = True
        while True:
            dis = maze[x][y]
            nx, ny = x + dx[d] * dis, y + dy[d] * dis

            if not (0 <= nx < N and 0 <= ny < M):
                flag = False
                break

            d = (d + 1) % 4
            x, y = nx, ny
            if visited[d][x][y]:
                result.append(i + 1)
                break
            else:
                visited[d][x][y] = True

    print(len(result))
    if result:
        print(*result)


N, M = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]
solution()
