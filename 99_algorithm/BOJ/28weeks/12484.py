def compute():
    x, s, r, t, n = map(int, input().split())
    ws = [list(map(int, input().split())) for i in range(n)]

    for w in ws:
        print(w)

    print('여기까지 ws')
    vs = list(map(lambda y: (r + y[2], y), ws))
    vs.append((r, [0, ws[0][0], 0]))
    for i in range(n - 1):
        vs.append((r, [ws[i][1], ws[i + 1][0], 0]))

    for vv in vs:
        print(vv)
    vs.append((r, [ws[n - 1][1], x, 0]))

    vs.sort()

    c = 0
    for _, q in enumerate(vs):
        tc = (q[1][1] - q[1][0]) * 1.0 / q[0]
        t -= tc
        c += tc
        if t < 0:
            break

    if t < 0:
        d = (q[1][1] - q[1][0]) - (tc + t) * q[0]
        c += t + d * 1.0 / (s + q[1][2])
        t = 0
        for i, j in vs[i + 1:]:
            c += (j[1] - j[0]) * 1.0 / (s + j[2])

    return c


for i in range(int(input())):
    print("Case #%d: %.8f" % (i + 1, compute()))
