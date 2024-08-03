import sys

input = sys.stdin.readline
N, M = map(int, input().split())

code = ['J', 'O', 'I']

K = int(input())
A = [input().rstrip() for _ in range(N)]

prefix_dict = dict()

for c in code:
    prefix_dict[c] = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        f = A[i][j]
        for c in code:
            prefix_dict[c][i + 1][j + 1] += prefix_dict[c][i][j + 1] + prefix_dict[c][i + 1][j] - prefix_dict[c][i][
                j]

        prefix_dict[f][i + 1][j + 1] += 1

for _ in range(K):
    x, y, xx, yy = map(int, input().split())
    rst = []
    for c in code:
        ans = prefix_dict[c][xx][yy] + prefix_dict[c][x - 1][y - 1] - prefix_dict[c][xx][y - 1] - prefix_dict[c][x - 1][
            yy]
        rst.append(str(ans))

    print(' '.join(rst))
