import sys
from collections import defaultdict

input = sys.stdin.readline

rsp_dict = {'S': 'P', 'P': 'R', 'R': 'S'}


def solve():
    for i in range(1, M + 1):
        for word, num in A[i].items():
            if 0 < num <= K:
                temp = ''
                for ww in word:
                    temp += rsp_dict[ww]
                return i, temp

    return -1, None


N, M, K = map(int, input().split())

cards = [input().rstrip() for _ in range(N)]

A = dict()

for i in range(1, M + 1):
    A[i] = defaultdict(int)

    for card in cards:
        A[i][card[:i]] += 1

rst, w = solve()

if rst != -1:
    print(rst)
    print(w)
else:
    print(-1)
