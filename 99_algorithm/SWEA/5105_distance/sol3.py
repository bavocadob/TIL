import sys

sys.stdin = open('input.txt')


def dfs(x, y):
    global find, result
    if (x, y) == end:
        find = True
        result = maze[x][y] - 2
        return
    if find:
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] == 0:
            maze[nx][ny] = maze[x][y] + 1
            dfs(nx, ny)
            maze[nx][ny] = 0


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

for tc in range(T):
    maze = []
    end = None
    start = None
    find = False
    result = 0
    size = int(input())

    for i in range(size):
        maze_line = input()
        if '2' in maze_line:
            start = (i, maze_line.index('2'))
        if '3' in maze_line:
            end = (i, maze_line.index('3'))

        maze.append(list(map(int, maze_line)))

    maze[end[0]][end[1]] = 0
    maze[start[0]][start[1]] = 1
    dfs(*start)

    print(f'#{tc+1} {result}')
