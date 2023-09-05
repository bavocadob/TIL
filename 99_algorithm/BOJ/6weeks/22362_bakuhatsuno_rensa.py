import sys

input = sys.stdin.readline
while True:
    N, M, num, distance, start = map(int, input().split())

    if (N, M, num, distance, start) == (0, 0, 0, 0, 0):
        break

    visited = [False] * num

    bombs = [tuple(map(int, input().split())) for _ in range(num)]

    stack = [bombs[start - 1]]
    visited[start - 1] = True

    while stack:
        x, y = stack.pop()

        for i in range(num):
            nx, ny = bombs[i]
            if not visited[i] and ((nx == x and abs(ny - y) <= distance) or (ny == y and abs(nx - x) <= distance)):
                visited[i] = True
                stack.append((nx, ny))

    print(sum(visited))
