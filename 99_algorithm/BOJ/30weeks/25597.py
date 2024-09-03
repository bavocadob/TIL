def solve(dist):
    eight = dist // 8

    dist -= eight * 8

    four = dist // 4

    dist -= four * 4

    one = dist

    if eight + four + one > T:
        print(-1)
        return

    if eight * 2 + four + one <= T:
        four += eight * 2
        eight = 0

    if eight + four * 4 + one <= T:
        one += four * 4
        four = 0

    print(int(eight > 0) + int(four > 0) + int(one > 0))
    curr = T - (one + four + eight)
    if eight:
        print(curr, 8)
        curr += eight

    if four:
        print(curr, 4)
        curr += four

    if one:
        print(curr, 1)


X, T = map(int, input().split())
solve(X)
