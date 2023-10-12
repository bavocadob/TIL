import sys

input = sys.stdin.readline


def init_map():
    if mine_map[0][0] == '1':
        mine_cnt[1][1] = 1
    if mine_map[0][N - 1] == '1':
        mine_cnt[1][N - 2] = 1
    if mine_map[N - 1][0] == '1':
        mine_cnt[N - 2][1] = 1
    if mine_map[N - 1][N - 1] == '1':
        mine_cnt[N - 2][N - 2] = 1


def solution():
    ans = 0
    for i in range(1, N - 2):
        mine_cnt[1][i + 1] = int(int(mine_map[0][i]) > mine_cnt[1][i] + mine_cnt[1][i - 1])

    for i in range(1, N - 2):
        mine_cnt[N - 2][i + 1] = int(int(mine_map[N - 1][i]) > mine_cnt[N - 2][i] + mine_cnt[N - 2][i - 1])

    for i in range(1, N - 2):
        mine_cnt[i + 1][1] = int(int(mine_map[i][0]) > mine_cnt[i][1] + mine_cnt[i - 1][1])

    for i in range(1, N - 2):
        mine_cnt[i + 1][N - 2] = int(int(mine_map[i][N - 1]) > mine_cnt[i][N - 2] + mine_cnt[i - 1][N - 2])

    for c in mine_cnt:
        ans += sum(c)

    if N >= 5:
        ans += (N - 4) ** 2

    return ans


N = int(input())

mine_map = [list(input()) for _ in range(N)]
mine_cnt = [[0] * N for _ in range(N)]

init_map()
print(solution())
