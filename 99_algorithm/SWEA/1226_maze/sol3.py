import sys

sys.stdin = open('input.txt')


def dfs(x, y):
    global find
    if (x, y) == end:
        find = True
        return
    if find:
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] != 1:
            maze[nx][ny] = 1
            dfs(nx, ny)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
size = 16

for _ in range(10):
    tc = int(input())
    maze = []
    start = None
    end = None
    find = False
    for i in range(16):
        maze_line = input()
        if '2' in maze_line:
            start = (i, maze_line.index('2'))
        if '3' in maze_line:
            end = (i, maze_line.index('3'))

        maze.append(list(map(int, maze_line)))

    dfs(*start)
    if find:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
