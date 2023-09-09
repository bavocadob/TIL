import sys

input = sys.stdin.readline

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def dfs(x, y):
    stack = [(x, y)]

    idx = maze[x][y]
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 0:
                    maze[nx][ny] = idx
                    size_dict[idx] += 1
                    stack.append((nx, ny))


N, M = map(int, input().split())

size_dict = dict()

maze = [list(map(int, input().rstrip())) for _ in range(N)]

dict_idx = 2

for i in range(N):
    for j in range(M):
        if maze[i][j] == 0:
            maze[i][j] = dict_idx
            size_dict[dict_idx] = 1
            dfs(i, j)
            dict_idx += 1

for i in range(N):
    for j in range(M):
        if maze[i][j] == 1:
            area_set = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] > 1:
                    area_set.add(maze[nx][ny])

            temp = 1
            for a in area_set:
                temp += size_dict[a]
            sys.stdout.write(str(temp % 10))
        else:
            sys.stdout.write('0')

    print()
