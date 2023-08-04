
m, n = map(int, input().split())


x, y = map(int, input().split())
city = [[0] * n for i in range(m)]

city[0][0] = 1


for i in range(x):
    for j in range(y):
        if i > 0:
            city[i][j] += city[i - 1][j] % 1_000_007

        if j > 0:
            city[i][j] += city[i][j - 1] % 1_000_007

        city[i][j] %= 1_000_007

for i in range(x - 1, m):
    for j in range(y - 1, n):
        if i > x - 1:
            city[i][j] += city[i - 1][j] % 1_000_007

        if j > y - 1:
            city[i][j] += city[i][j - 1] % 1_000_007

        city[i][j] %= 1_000_007


print(city[m - 1][n - 1])