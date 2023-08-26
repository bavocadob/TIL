import sys


def can_charge(people_x, people_y, charger_x, charger_y, charger_distance):
    d = abs(people_x - charger_x) + abs(people_y - charger_y)
    return charger_distance >= d


sys.stdin = open('input.txt')

dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

T = int(input())

for tc in range(T):

    a_index = [1, 1]
    b_index = [10, 10]

    move, bc_num = map(int, input().split())

    a_move = [0] + list(map(int, input().split()))
    b_move = [0] + list(map(int, input().split()))

    bc_list = []
    for _ in range(bc_num):
        x, y, c, p = map(int, input().split())
        bc_list.append((x, y, c, p))

    ans = 0

    for i in range(move + 1):
        a_index[0] += dx[a_move[i]]
        a_index[1] += dy[a_move[i]]
        b_index[0] += dx[b_move[i]]
        b_index[1] += dy[b_move[i]]

        a_bc_lst = list()
        b_bc_lst = list()

        for k in range(bc_num):
            x, y, c, p = bc_list[k]

            if can_charge(a_index[0], a_index[1], x, y, c):
                a_bc_lst.append((p, k))

            if can_charge(b_index[0], b_index[1], x, y, c):
                b_bc_lst.append((p, k))

        a_bc_lst.sort(reverse=True)
        b_bc_lst.sort(reverse=True)
        # print(a_bc_lst, b_bc_lst)
        if a_bc_lst and b_bc_lst:
            if a_bc_lst[0] != b_bc_lst[0]:
                ans += a_bc_lst[0][0] + b_bc_lst[0][0]
            elif len(a_bc_lst) == 1 and len(b_bc_lst) == 1:
                ans += a_bc_lst[0][0]
            elif len(a_bc_lst) == 1 and len(b_bc_lst) > 1:
                ans += a_bc_lst[0][0] + b_bc_lst[1][0]
            elif len(a_bc_lst) > 1 and len(b_bc_lst) == 1:
                ans += a_bc_lst[1][0] + b_bc_lst[0][0]
            else:
                ans += a_bc_lst[0][0] + max(a_bc_lst[1][0], b_bc_lst[1][0])
        elif a_bc_lst:
            ans += a_bc_lst[0][0]
        elif b_bc_lst:
            ans += b_bc_lst[0][0]

    print(f'#{tc + 1} {ans}')
