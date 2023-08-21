import sys

sys.stdin = open('input.txt')

# 오델로 돌을 놓았을 때 가능한 변경을 찾기 위한 8방탐색
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]

    board[N // 2][N // 2] = board[(N - 1) // 2][(N - 1) // 2] = 2
    board[N // 2][(N - 1) // 2] = board[(N - 1) // 2][N // 2] = 1

    for _ in range(M):

        x, y, color = map(int, input().split())
        x, y = y - 1, x - 1
        board[x][y] = color
        for k in range(8):
            distance = 1
            can_change = False
            while True:
                nx, ny = x + dx[k] * distance, y + dy[k] * distance

                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == color:
                        print(nx,ny, distance)
                        can_change = True
                        break
                    elif board[nx][ny] != 0:
                        distance += 1
                    else:
                        break
                else:
                    break

            if can_change:
                for d in range(1, distance):

                    nx, ny = x + dx[k] * distance, y + dy[k] * distance
                    print('변화', nx,ny, d, x, y)
                    board[nx][ny] = color

        for line in board:
            print(line)
        print()
