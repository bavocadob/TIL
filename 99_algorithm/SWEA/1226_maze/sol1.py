import sys

from collections import deque

sys.stdin = open('input.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
size = 16

for _ in range(10):
    tc = int(input())
    maze = []
    queue = deque()
    end = None

    for i in range(16):
        maze_line = input()
        if '2' in maze_line:
            queue.append((i, maze_line.index('2')))
        if '3' in maze_line:
            end = (i, maze_line.index('3'))

        maze.append(list(map(int,maze_line)))

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            print(f'#{tc} {1}')
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] != 1:
                maze[nx][ny] = 1
                queue.append((nx, ny))
    else:
        print(f'#{tc} {0}')


