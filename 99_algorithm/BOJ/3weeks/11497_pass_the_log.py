import sys

from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())

    log_list = list(map(int, input().split()))
    log_list.sort()

    queue = deque([log_list.pop()])
    while log_list:
        log = log_list.pop()
        if queue[-1] > queue[0]:
            queue.append(log)
        else:
            queue.appendleft(log)

    max_gap = 0
    for i in range(len(queue)):
        max_gap = max(max_gap, abs(queue[i] - queue[i - 1]))
    print(max_gap)

