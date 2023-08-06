# 백준 28420 카더가든
# 누적합 + 브루트포스
# 코드를 깔끔하게 하려면 메소드로 나눠서 구간합 계산을 따로 빼야할 것 같다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

width, a_height, b_height = map(int, input().split())

garden = [list(map(int, input().split())) for _ in range(N)]

prefix_sum = [[0] * (M + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = garden[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

min_fog = int(1e9)

a_length = (a_height + b_height)

for i in range(1, N + 2 - width):
    for j in range(1, M + 2 - a_length):
        min_fog = min(prefix_sum[i + width - 1][j + a_length - 1] + prefix_sum[i - 1][j - 1] - prefix_sum[i - 1][
            j + a_length - 1] - prefix_sum[i + width - 1][j - 1], min_fog)

for i in range(N + 1 - (width + a_height)):
    for j in range(M + 1 - (width + b_height)):
        sum_a = prefix_sum[i + width][j + b_height] + prefix_sum[i][j] - prefix_sum[i][j + b_height] - \
                prefix_sum[i + width][j]
        sum_b = prefix_sum[i + width + a_height][j + width + b_height] + prefix_sum[i + width][j + b_height] - \
                prefix_sum[i + width + a_height][j + b_height] - prefix_sum[i + width][j + width + b_height]
        min_fog = min(min_fog, sum_a + sum_b)


for i in range(N + 1 - (width + b_height)):
    for j in range(M + 1 - (width + a_height)):
        sum_a = prefix_sum[i + width][j + a_height] + prefix_sum[i][j] - prefix_sum[i][j + a_height] - \
                prefix_sum[i + width][j]
        sum_b = prefix_sum[i + width + b_height][j + width + a_height] + prefix_sum[i + width][j + a_height] - \
                prefix_sum[i + width + b_height][j + a_height] - prefix_sum[i + width][j + width + a_height]
        min_fog = min(min_fog, sum_a + sum_b)

print(min_fog)