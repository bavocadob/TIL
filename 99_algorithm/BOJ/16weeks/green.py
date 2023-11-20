def draw(depth, x, y):
    if depth == 0:
        star[x][y] = '*'
        return
    interval = 5 ** (depth - 1)

    for i in range(5):
        for j in range(5):
            if i == 0 or i == 1:
                if j != 2:
                    continue
            if i == 3 and (j == 0 or j == 4):
                continue

            if i == 4 and (j != 1 and j != 3):
                continue

            draw(depth - 1, x + interval * i, y + interval * j)


N = int(input())
star = [[' '] * (5 ** N) for _ in range(5 ** N)]
draw(N, 0, 0)
for s in star:
    print(''.join(s))
