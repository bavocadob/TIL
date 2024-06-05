from collections import deque

INF = int(1e9)

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

ws, bs, we, be = input().split()

ws_x = ord(ws[0]) - ord('a')
ws_y = int(ws[1]) - 1

bs_x = ord(bs[0]) - ord('a')
bs_y = int(bs[1]) - 1

we_x = ord(we[0]) - ord('a')
we_y = int(we[1]) - 1

be_x = ord(be[0]) - ord('a')
be_y = int(be[1]) - 1

dp = [[[[(INF, -1, -1, -1, -1)] * 8 for _ in range(8)] for _ in range(8)] for _ in range(8)]

dp[ws_x][ws_y][bs_x][bs_y] = (0, -1, -1, -1, -1)

queue = deque([(ws_x, ws_y, bs_x, bs_y)])

while queue:
    wx, wy, bx, by = queue.popleft()

    curr_dist = dp[wx][wy][bx][by][0]

    for k in range(8):
        nwx, nwy = wx + dx[k], wy + dy[k]

        if (nwx, nwy) == (bx, by):
            continue

        if not (0 <= nwx < 8 and 0 <= nwy < 8):
            continue

        if curr_dist + 1 < dp[nwx][nwy][bx][by][0]:
            dp[nwx][nwy][bx][by] = (curr_dist + 1, wx, wy, bx, by)
            queue.append((nwx, nwy, bx, by))

    for k in range(8):
        nbx, nby = bx + dx[k], by + dy[k]

        if (nbx, nby) == (wx, wy):
            continue

        if not (0 <= nbx < 8 and 0 <= nby < 8):
            continue

        if curr_dist + 1 < dp[wx][wy][nbx][nby][0]:
            dp[wx][wy][nbx][nby] = (curr_dist + 1, wx, wy, bx, by)
            queue.append((wx, wy, nbx, nby))

print(dp[we_x][we_y][be_x][be_y][0])

rst = []

while not (we_x == ws_x and we_y == ws_y and be_x == bs_x and be_y == bs_y):
    _, nwx, nwy, nbx, nby = dp[we_x][we_y][be_x][be_y]

    # 흰색이 안움직인거면 검은색이 움직인 것
    if nwx == we_x and nwy == we_y:
        str_x = chr(be_x + ord('a'))
        str_y = str(be_y + 1)
        rst.append(('B', str_x + str_y))
    else:
        str_x = chr(we_x + ord('a'))
        str_y = str(we_y + 1)
        rst.append(('W', str_x + str_y))

    we_x, we_y, be_x, be_y = nwx, nwy, nbx, nby

rst.reverse()
for color, idx in rst:
    print(color, idx)
