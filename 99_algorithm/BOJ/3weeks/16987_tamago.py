max_cnt = 0

def crash(depth, cnt):
    global max_cnt
    if depth == N or max_cnt == N:
        max_cnt = max(max_cnt, cnt)

        return

    if tamago[depth][0] <= 0:
        crash(depth + 1, cnt)
    else:
        hit = False
        for i in range(N):
            if i != depth and tamago[i][0] > 0:
                tamago[i][0] -= tamago[depth][1]
                tamago[depth][0] -= tamago[i][1]

                temp_cnt = 0

                if tamago[i][0] <= 0:
                    temp_cnt += 1
                if tamago[depth][0] <= 0:
                    temp_cnt += 1

                hit = True
                crash(depth + 1, cnt + temp_cnt)

                tamago[i][0] += tamago[depth][1]
                tamago[depth][0] += tamago[i][1]

        if not hit:
            crash(depth + 1, cnt)


N = int(input())

tamago = [list(map(int, input().split())) for _ in range(N)]
crash(0, 0)
print(max_cnt)
