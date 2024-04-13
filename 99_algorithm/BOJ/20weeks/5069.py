dy = [-1, 0, 1, 1, 0, -1]
dx = [0, 1, 1, 0, -1, -1]


def solve(y, x, temp):
    if temp == 0:
        return int(y == 0 and x == 0)
    if (y, x, temp) in dp:
        return dp[(y, x, temp)]

    ret = 0
    for d in range(6):
        ny = y + dy[d]
        nx = x + dx[d]
        ret += solve(ny, nx, temp - 1)

    dp[(y, x, temp)] = ret
    return ret


T = int(input())

for _ in range(T):
    N = int(input())
    dp = {}
    print(solve(0, 0, N))
