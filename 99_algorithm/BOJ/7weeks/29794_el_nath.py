import sys

sys.stdin = open('input.txt')

N, M, K = map(int, input().split())

day_sum = [0] * (M + 1)

level = list(map(int, input().split()))
level_table = [0] * 201
for i in range(N):
    level_table[level[i]] += 1

tower = list(map(int, input().split())) + [200]

for i in range(M + 1):
    tower[i] = (tower[i], i + 1)

tower.sort()

for i in range(1, 200):
    if level_table[i] == 0:
        continue
    curr_level = i
    day = K
    for j in range(M):
        if tower[j][0] <= curr_level < tower[j + 1][0]:
            level_up = min(day, tower[j + 1][0] - curr_level)
            day -= level_up
            curr_level += level_up
            day_sum[tower[j][1]] += level_up * level_table[i]
            if day == 0 or curr_level == 200:
                break

move_sum = 0
for i in range(1, M + 1):
    move_sum += (i - 1) * day_sum[i]

move_min = move_sum

left = 1
right = 2

for i in range(1, M):
    for j in range(i + 1, M + 1):
        temp_move = 0
        for k in range(1, M + 1):
            temp_move += min(abs(k - i) + i - 1, abs(k - j)) * day_sum[k]
            if temp_move > move_min:
                break

        if move_min > temp_move:
            move_min = temp_move
            left = i
            right = j


print(left, right)
print(move_sum - move_min)
