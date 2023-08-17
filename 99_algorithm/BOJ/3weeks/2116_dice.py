import sys

input = sys.stdin.readline


def solution(t_val):
    dice_sum = 0
    for i in range(N):
        tail_index = dices[i].index(t_val)
        head_index = dice_dict[tail_index]
        h_val = dices[i][head_index]

        if 5 in [h_val, t_val] and 6 in [h_val, t_val]:
            dice_sum += 4
        elif 6 in [h_val, t_val]:
            dice_sum += 5
        else:
            dice_sum += 6

        t_val = h_val
    return dice_sum


dice_dict = {0: 5, 5: 0, 2: 4, 4: 2, 1: 3, 3: 1}

N = int(input())

dices = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0
for i in range(1, 7):
    temp_sum = solution(i)
    max_sum = max(max_sum, temp_sum)

print(max_sum)
