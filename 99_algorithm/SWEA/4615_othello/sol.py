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
                    nx, ny = x + dx[k] * d, y + dy[k] * d
                    board[nx][ny] = color

        w_count = 0
        b_count = 0
    for board_line in board:
        b_count += board_line.count(1)
        w_count += board_line.count(2)

    print(f'#{tc+1} {b_count} {w_count}')
