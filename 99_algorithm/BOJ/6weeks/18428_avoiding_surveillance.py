N = int(input())
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def valid(x, y):
    return 0 <= x < N and 0 <= y < N


# 둘 가치 판단
def valuable(x, y):
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        while valid(nx, ny):
            if room[nx][ny] == 'O':
                break
            elif room[nx][ny] == 'T':
                kk = (k + 2) % 4
                nnx, nny = x + dx[kk], y + dy[kk]
                while valid(nnx, nny):
                    if room[nnx][nny] == 'S':
                        return True
                    elif room[nnx][nny] == 'O':
                        break
                    nnx, nny = nnx + dx[kk], nny + dy[kk]
                break
            nx, ny = nx + dx[k], ny + dy[k]
    return False


def avoid():
    global result
    for teacher in teachers:
        x, y = teacher

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            while valid(nx, ny):
                if room[nx][ny] == 'O':
                    break
                elif room[nx][ny] == 'S':
                    return False
                nx, ny = nx + dx[k], ny + dy[k]

    result = True
    return True


# X를 O로 바꿀 가치가 있는지 (상하혹은 좌우에 T와 S가 존재하는지를 기준으로 백트래킹
def backtrack(idx, depth):
    global result
    if result or avoid():
        return
    if depth == 3:
        return

    for i in range(idx, len(candidate)):
        x, y = candidate[i]
        if valuable(x, y):
            room[x][y] = 'O'
            backtrack(i + 1, depth + 1)
            room[x][y] = 'X'


room = [input().split() for _ in range(N)]

candidate = []
teachers = []

for i in range(N):
    for j in range(N):
        if room[i][j] == 'X':
            candidate.append((i, j))
        elif room[i][j] == 'T':
            teachers.append((i, j))

result = False
backtrack(0, 0)


if result:
    print('YES')
else:
    print('NO')
