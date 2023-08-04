
def check1(x, y):
    cnt = 1
    temp_x = x + 1
    temp_y = y + 1

    while temp_x < 19 and temp_y < 19 and gomoku_board[temp_x][temp_y] == gomoku_board[x][y]:
        cnt += 1
        temp_x += 1
        temp_y += 1

    temp_x = x - 1
    temp_y = y - 1

    while temp_x >= 0 and temp_y >= 0 and gomoku_board[temp_x][temp_y] == gomoku_board[x][y]:
        cnt += 1
        temp_x -= 1
        temp_y -= 1

    return cnt == 5


def check2(x, y):
    cnt = 1
    temp_x = x - 1
    temp_y = y + 1

    while temp_x >= 0 and temp_y < 19 and gomoku_board[temp_x][temp_y] == gomoku_board[x][y]:
        cnt += 1
        temp_x -= 1
        temp_y += 1

    temp_x = x + 1
    temp_y = y - 1

    while temp_x < 19 and temp_y >= 0 and gomoku_board[temp_x][temp_y] == gomoku_board[x][y]:
        cnt += 1
        temp_x += 1
        temp_y -= 1

    return cnt == 5


def check3(x, y):
    cnt = 1
    temp_x = x + 1

    while temp_x < 19 and gomoku_board[temp_x][y] == gomoku_board[x][y]:
        cnt += 1
        temp_x += 1

    temp_x = x - 1

    while temp_x >= 0 and gomoku_board[temp_x][y] == gomoku_board[x][y]:
        cnt += 1
        temp_x -= 1

    return cnt == 5


def check4(x, y):
    cnt = 1
    temp_y = y + 1

    while temp_y < 19 and gomoku_board[x][temp_y] == gomoku_board[x][y]:
        cnt += 1
        temp_y += 1

    temp_y = y - 1

    while temp_y >= 0 and gomoku_board[x][temp_y] == gomoku_board[x][y]:
        cnt += 1
        temp_y -= 1

    return cnt == 5


# 19 * 19 오목판 생성
gomoku_board = [list(map(int, input().split())) for _ in range(19)]

game_end = False
for i in range(19):
    for j in range(19):
        if gomoku_board[i][j] != 0:
            game_end = check1(i, j) or check2(i, j) or check3(i, j) or check4(i, j)
            if game_end and not check2(i,j):
                print(gomoku_board[i][j])
                print(i + 1, j + 1)
                break
            elif game_end and check2(i, j):
                print(gomoku_board[i][j])
                print(i + 5, j - 3)
                break

    if game_end:
        break

if not game_end:
    print(0)


