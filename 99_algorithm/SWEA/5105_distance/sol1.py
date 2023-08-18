import sys

from collections import deque

sys.stdin = open('input.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

for tc in range(T):
    maze = []
    queue = deque()
    end = None
    start = None
    size = int(input())

    for i in range(size):
        maze_line = input()
        if '2' in maze_line:
            queue.append((i, maze_line.index('2')))
            start = (i, maze_line.index('2'))
        if '3' in maze_line:
            end = (i, maze_line.index('3'))

        maze.append(list(map(int,maze_line)))

    maze[end[0]][end[1]] = 0
    maze[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            print(f'#{tc + 1} {maze[x][y] - 2}')
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] == 0:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    else:
        print(f'#{tc + 1} {0}')


