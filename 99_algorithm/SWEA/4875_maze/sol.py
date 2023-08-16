import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    maze = []
    stack = []
    target = None

    for i in range(N):
        line = list(map(int, input()))
        for j in range(N):
            if line[j] == 2:
                stack.append((i, j))
            elif line[j] == 3:
                target = (i, j)
        maze.append(line)

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    while stack:
        x, y = stack.pop()
        if (x, y) == target:
            print(f'#{T} 1')
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1:
                maze[nx][ny] = 1
                stack.append((nx, ny))
    else:
        print(f'#{tc+1} 0')
