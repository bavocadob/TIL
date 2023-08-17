import sys

sys.stdin = open('input.txt')

from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    pizzas.reverse()

    oven = deque()
    for i in range(N):
        oven.append((pizzas.pop(), i + 1))

    while oven:
        pizza, pizza_index = oven.popleft()

        if not oven:
            print(f'#{tc + 1} {pizza_index}')
            break

        if pizza // 2 == 0 and pizzas:
            oven.appendleft((pizzas.pop(), N + 1))
            N += 1
        elif pizza // 2 > 0:
            oven.append((pizza // 2, pizza_index))
