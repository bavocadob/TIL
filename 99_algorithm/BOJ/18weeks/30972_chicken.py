def get_sum(x1, y1, x2, y2):
    return pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1]


N = int(input())

chicken = [list(map(int, input().split())) for _ in range(N)]

pre = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        pre[i][j] = chicken[i - 1][j - 1] + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1]

for p in pre:
    print(p)

Q = int(input())

for _ in range(Q):
    i1, j1, i2, j2 = map(int, input().split())
    ans = get_sum(i1 + 1, j1 + 1, i2 - 1, j2 - 1)
    ans -= get_sum(i1, j1, i2, j1) + get_sum(i1, j1, i1, j2) + get_sum(i1, j2, i2, j2) + get_sum(i2, j1, i2, j2)
    ans += get_sum(i1, j1, i1, j1) + get_sum(i2, j1, i2, j1) + get_sum(i1, j2, i1, j2) + get_sum(i2, j2, i2, j2)
    print(ans)
