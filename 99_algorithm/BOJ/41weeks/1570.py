def solve():
    n, sx, sy, mx, my = map(int, input().split())
    mx -= sx
    my -= sy

    if mx < 0 or my < 0:
        return "-1"

    if mx == 0:
        up_moves = min(my, n)
        right_moves = n - up_moves
        return "U" * up_moves + "R" * right_moves

    ans = set()

    for x in range(n, 0, -1):
        y = n - x
        h = (mx // x) * y
        if my - y <= h <= my + y:
            x1 = mx % x  # 나머지 x 이동
            x2 = x - x1  # 나머지 x 이동 보완
            y1 = my - h  # y에서 필요한 상단 이동
            y2 = y - y1  # 나머지 y 이동 보완

            # 불가능한 경로 배제
            if x1 > 0 and y1 < 0:
                continue
            if x1 == 0 and y1 < 0:
                y2 += y1
                y1 = 0

            path = "R" * x1 + "U" * y1 + "R" * x2 + "U" * y2
            ans.add(path)

    if not ans:
        return "-1"

    return min(ans)


print(solve())
