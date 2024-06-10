import sys
from collections import defaultdict

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def move():
    separate_queue = set()
    new_queue_dict = defaultdict(list)

    while queue:
        i, j, weight, speed, direction = queue.pop()

        ni, nj = (i + dx[direction] * speed) % N, (j + dy[direction] * speed) % N

        new_queue_dict[(ni, nj)].append((weight, speed, direction))

        if len(new_queue_dict[(ni, nj)]) > 1:
            separate_queue.add((ni, nj))

    for x, y in separate_queue:

        fireball_list = new_queue_dict[(x, y)]

        fireball_len = len(fireball_list)
        is_odd = False

        weight_sum = 0
        speed_sum = 0
        for i in range(fireball_len):
            weight_sum += fireball_list[i][0]
            speed_sum += fireball_list[i][1]

            if fireball_list[i][2] % 2 != fireball_list[i - 1][2] % 2:
                is_odd = True

        new_weight = weight_sum // 5
        new_speed = speed_sum // fireball_len

        new_fireball_list = []
        start_idx = int(is_odd)

        if new_weight > 0:
            for i in range(start_idx, 8, 2):
                new_fireball_list.append((new_weight, new_speed, i))

        del fireball_list
        new_queue_dict[(x, y)] = new_fireball_list

    for x, y in new_queue_dict.keys():
        for weight, speed, direction in new_queue_dict[(x, y)]:
            queue.append((x, y, weight, speed, direction))


N, M, K = map(int, input().split())

queue = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1

    queue.append((r, c, m, s, d))

for _ in range(K):
    move()

ans = 0
for i in range(len(queue)):
    ans += queue[i][2]

print(ans)
