import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ddx = [1, 0, -1, 0]
ddy = [0, 1, 0, -1]


def valid(x, y):
    return 0 <= x < N and 0 <= y < M


def diffusion():
    global change
    # flag = False
    for i in range(N):
        for j in range(M):
            if room[i][j] > 0:
                dust = room[i][j] // 5

                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if valid(ni, nj) and (ni, nj) not in purifier:
                        change[ni][nj] += dust
                        change[i][j] -= dust

    for i in range(N):
        for j in range(M):
            room[i][j] += change[i][j]
            # if change[i][j] > 0:
            # flag = True
    change = [[0] * M for _ in range(N)]
    # return flag


def purify():
    x, y = purifier[0]
    x -= 1

    idx = 0

    # 위에거 청정
    while True:
        while True:
            nx, ny = x + dx[idx], y + dy[idx]
            if 0 <= nx <= purifier[0][0] and 0 <= ny < M and (nx, ny) != purifier[0]:

                room[x][y] = room[nx][ny]
                x, y = nx, ny
            else:
                break
        idx += 1
        if idx == 4:
            room[x][y] = 0
            break

    x, y = purifier[1]
    x += 1
    idx = 0
    while True:
        while True:
            nx, ny = x + ddx[idx], y + ddy[idx]
            if purifier[1][0] <= nx < N and 0 <= ny < M and (nx, ny) != purifier[1]:
                room[x][y] = room[nx][ny]
                x, y = nx, ny
            else:
                break
        idx += 1
        if idx == 4:
            room[x][y] = 0
            break


N, M, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
change = [[0] * M for _ in range(N)]
purifier = []

for i in range(N):
    if room[i][0] == -1:
        purifier.append((i, 0))
        purifier.append((i + 1, 0))
        break

for _ in range(T):
    diffusion()
    purify()

ans = 2
for i in range(N):
    ans += sum(room[i])

print(ans)
