import sys

from math import ceil

input = sys.stdin.readline


def upper_bound(target):
    left = 0
    right = K
    while left < right:
        mid = (left + right) // 2

        if curr_score[mid][0] <= target:
            left = mid + 1
        else:
            right = mid
    return left


K, N, M = map(int, input().split())

threshold_cnt = ceil(K / 12)

winner = []
candidate = []

curr_score = [(int(input()), i) for i in range(K)]
curr_score.sort()

if N == M:
    gold_value = curr_score[K - (K + 11) // 12][0]
    for i in range(K):
        if curr_score[i][0] >= gold_value:
            winner.append(curr_score[i][1] + 1)
            candidate.append(curr_score[i][1] + 1)
else:
    for i in range(K):
        # 최악의 경우(나빼고 다 100점, 나는 0점)에도 금메달을 딸 수 있는지 조사
        my_score = curr_score[i][0] - (100 * (N - M))
        cnt = K - upper_bound(my_score) - 1
        if cnt < threshold_cnt:
            winner.append(curr_score[i][1] + 1)

        # 최선의 경우 (나만 100점)
        my_score = curr_score[i][0] + (100 * (N - M))

        cnt = K - upper_bound(my_score)
        # print(my_score, '점수', cnt, '나보다 높은놈')
        if cnt < threshold_cnt:
            candidate.append(curr_score[i][1] + 1)

winner.sort()
candidate.sort()

# result_data = '\n'.join(map(str, winner)) + '\n--------\n' + '\n'.join(map(str, candidate))
# print(result_data)

for win in winner:
    print(win, end='\n')

print('--------')

for can in candidate:
    print(can, end='\n')
