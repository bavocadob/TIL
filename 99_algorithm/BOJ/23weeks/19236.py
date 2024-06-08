from copy import deepcopy

size = 4


def rotate(field, shark_x, shark_y):
    fish_list = [None] * ((size * size) + 1)

    for i in range(size):
        for j in range(size):
            if field[i][j] is None:
                continue

            idx, direction = field[i][j]
            fish_list[idx] = (i, j)

    for i in range(1, size * size + 1):
        if fish_list[i] is None:
            continue

        fish_x, fish_y = fish_list[i]
        idx, direction = field[fish_x][fish_y]

        for k in range(8):

            nx, ny = fish_x + dx[direction], fish_y + dy[direction]

            if not (0 <= nx < size and 0 <= ny < size) or (nx, ny) == (shark_x, shark_y):
                direction = (direction % 8) + 1
                continue

            if field[nx][ny] is not None:
                nidx, ndir = field[nx][ny]

                field[fish_x][fish_y] = (nidx, ndir)
                fish_list[nidx] = (fish_x, fish_y)
            else:
                field[fish_x][fish_y] = None

            field[nx][ny] = (idx, direction)
            fish_list[idx] = (nx, ny)
            break


def dfs(field, shark_x, shark_y, score):
    global ans

    fish_idx, fish_dir = field[shark_x][shark_y]
    score += fish_idx

    if score > ans:
        ans = score

    shark_dir = fish_dir
    curr_field = deepcopy(field)
    curr_field[shark_x][shark_y] = None

    rotate(curr_field, shark_x, shark_y)

    while True:
        nx, ny = shark_x + dx[shark_dir], shark_y + dy[shark_dir]

        if not (0 <= nx < size and 0 <= ny < size):
            break

        if curr_field[nx][ny] is not None:
            dfs(curr_field, nx, ny, score)

        shark_x, shark_y = nx, ny


dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

A = []

for _ in range(size):
    temp = list(map(int, input().split()))
    temp_list = []
    for j in range(size):
        a, b = temp[j * 2], temp[j * 2 + 1]
        temp_list.append((a, b))
    A.append(temp_list)

ans = 0

dfs(A, 0, 0, 0)

print(ans)
