import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):

    N, k = map(int, input().split())

    size = N // 4
    password = input()
    p_queue = deque(list(password))

    hex_set = set()

    for _ in range(size):
        p_queue.appendleft(p_queue.pop())
        for i in range(0, N, size):
            s = ''
            for j in range(size):
                s += p_queue[i + j]
            hex_set.add(s)

    hex_list = sorted(list(hex_set), reverse=True)

    print(f'#{tc + 1} {int(hex_list[k - 1], base=16)}')
