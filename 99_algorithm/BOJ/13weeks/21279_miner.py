import heapq
import sys

input = sys.stdin.readline

mines = []


def pop_mines(cost):
    curr_y = -mines[0][0]
    minus = 0
    while len(mines) > cost:
        temp_y = -mines[0][0]

        while mines and -mines[0][0] == temp_y:
            _, minus_value = heapq.heappop(mines)
            minus += minus_value

        curr_y = temp_y - 1
    return curr_y, minus


def solution():
    ans = 0
    temp_value = 0
    x_idx = 0
    y_idx = 100_000

    while x_idx <= 100_000:
        for y_, v_ in x_mine[x_idx]:
            if y_ <= y_idx:
                temp_value += v_
                heapq.heappush(mines, (-y_, v_))

        if len(mines) > C:
            y_idx, minus = pop_mines(C)
            temp_value -= minus

        ans = max(temp_value, ans)
        x_idx += 1

    return ans


N, C = map(int, input().split())

x_mine = [list() for _ in range(100001)]

for _ in range(N):
    x, y, v = map(int, input().split())
    x_mine[x].append((y, v))

print(solution())
