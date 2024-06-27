import sys
from collections import deque

input = sys.stdin.readline

visited = dict()
visited[1] = ['C+1']
visited[-1] = ['C-1']

queue = deque()

queue.append((1, ['C+1']))
queue.append((-1, ['C-1']))
while queue:
    curr, route = queue.popleft()
    if -32768 <= curr * 2 <= 32767 and curr * 2 not in visited:
        temp = route + ['DBL']
        visited[curr * 2] = temp
        queue.append((curr * 2, temp))

    if -32768 <= curr + 1 <= 32767 and curr + 1 not in visited:
        temp = route + ['INCR']
        visited[curr + 1] = temp
        queue.append((curr + 1, temp))

while True:
    N = int(input())

    if N == 0:
        break

    if N in visited:
        print(f'Constant {N}')
        print('\n'.join(visited[N]))
        print('')
        continue
