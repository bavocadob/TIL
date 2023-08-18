from collections import deque

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    command = input().rstrip().replace('RR', '')
    N = int(input())

    arr = []
    if N > 0:
        arr_str = input().rstrip()
        arr_str = arr_str[1:len(arr_str) - 1]
        arr = list(map(int, arr_str.split(',')))
    else:
        input().rstrip()

    queue = deque(arr)

    reverse = False
    valid = True

    for c in command:
        if c == 'R':
            reverse = not reverse
            continue
        if queue:
            if reverse:
                queue.pop()
            else:
                queue.popleft()
        else:
            valid = False
            break

    if valid:
        arr = list(queue)
        if reverse:
            arr.reverse()
        print('[', end='')
        print(','.join(map(str,arr)), end='')
        print(']')
    else:
        print('error')



