import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 0 1 2 3 = 북동남서

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

*curr_index, cp = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

clean_cnt = 0

while True:
    x, y = curr_index
    if room[x][y] == 0:
        room[x][y] = -1
        clean_cnt += 1

    can_move = False
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            can_move = True
            break

    if can_move:
        while True:
            cp = (cp - 1) % 4
            nx, ny = x + dx[cp], y + dy[cp]
            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                curr_index = (nx, ny)
                break
    else:
        nx, ny = x - dx[cp], y - dy[cp]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == -1:
            curr_index = (nx, ny)
        else:
            break

print(clean_cnt)
