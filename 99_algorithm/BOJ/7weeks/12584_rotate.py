T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    board = []

    for _ in range(N):
        line = input().rstrip().replace('.', '')
        board.append(list('.' * (N - len(line)) + line))

    # for b input.txt board:
    #     print(b)

    win = {'R': False, 'B': False}
    # 가로
    for i in range(N):
        curr = board[i][0]
        length = 0
        for j in range(N):
            if board[i][j] != '.':
                if curr != board[i][j]:
                    curr = board[i][j]
                    length = 1
                else:
                    length += 1
                    if length == K:
                        win[board[i][j]] = True

    # 세로
    for j in range(N):
        curr = board[0][j]
        length = 0
        for i in range(N):
            if board[i][j] != '.':
                if curr != board[i][j]:
                    curr = board[i][j]
                    length = 1
                else:
                    length += 1
                    if length == K:
                        win[board[i][j]] = True

    # 대각선 좌상 우하

    # 좌상우하 윗
    for i in range(N):
        curr = board[i][0]
        length = 0
        for j in range(i + 1):
            if board[i - j][j] != '.':
                if curr != board[i - j][j]:
                    curr = board[i - j][j]
                    length = 1
                else:
                    length += 1
                    if length == K:
                        win[board[i - j][j]] = True

    # 좌상우하 밑

    for i in range(1, N):
        curr = board[i][N - 1]
        length = 0
        for j in range(N - i):
            if board[i + j][N - j - 1] != '.':
                if curr != board[i + j][N - j - 1]:
                    curr = board[i + j][N - j - 1]
                    length = 1
                else:
                    length += 1
                    if length == K:
                        win[board[i + j][N - j - 1]] = True
    # 대각선 우상 좌하
    # 우상좌하 윗
    for j in range(N):
        curr = board[0][j]
        length = 0
        for i in range(N - j):
            if board[i][j + i] != '.':
                if curr != board[i][j + i]:
                    curr = board[i][j + i]
                    length = 1
                else:
                    length += 1
                    if length == K:
                        win[board[i][j + i]] = True

    # 우상좌하 밑
    for i in range(1, N):
        curr = board[i][0]
        length = 0
        for j in range(N - i):
            if board[i + j][j] != '.':
                if curr != board[i + j][j]:
                    curr = board[i + j][j]
                    length = 1
                else:
                    length += 1
                    if length == K:
                        win[board[i + j][j]] = True

    if win['R'] and win['B']:
        result = 'Both'
    elif win['R'] and not win['B']:
        result = 'Red'
    elif win['B'] and not win['R']:
        result = 'Blue'
    else:
        result = 'Neither'

    print(f'Case #{tc + 1}: {result}')
