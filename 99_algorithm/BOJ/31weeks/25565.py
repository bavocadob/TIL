import sys

input = sys.stdin.readline


def solve():
    _sum = sum([sum(f) for f in fields])

    if K * 2 == _sum:
        print(0)
        return

    x_min, y_min = N, M
    x_max = y_max = 0

    for i in range(N):
        for j in range(M):
            if fields[i][j] == 0:
                continue
            x_min = min(x_min, i)
            y_min = min(y_min, j)
            x_max = max(x_max, i)
            y_max = max(y_max, j)

    if x_max == x_min:
        size = K * 2 - sum(fields[x_max])
        print(size)

        for i in range(y_min + 1 + K - size, y_min + K + 1):
            print(x_min + 1, i)

        return

    if y_max == y_min:
        size = K * 2
        for i in range(N):
            size -= fields[i][y_max]

        print(size)

        for i in range(x_min + 1 + K - size, x_min + K + 1):
            print(i, y_min + 1)

        return

    ans_x = ans_y = 0
    while sum(fields[ans_x]) != K:
        ans_x += 1

    while True:
        temp = 0
        for i in range(N):
            temp += fields[i][ans_y]

        if temp == K:
            break

        ans_y += 1

    print(1)
    print(ans_x + 1, ans_y + 1)


N, M, K = map(int, input().split())

fields = [list(map(int, input().split())) for _ in range(N)]
solve()
