import sys

sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(T):
    a, b = map(int, input().split())

    queue = deque([(a, 0)])
    visited = [False] * (b * 3)
    visited[a] = True

    while queue:
        n, cnt = queue.popleft()
        # print(n, cnt)
        if n == b:
            print(f'#{tc + 1} {cnt}')
            break

        if n > 10:
            if not visited[n - 10]:
                visited[n - 10] = True
                queue.append((n - 10, cnt + 1))
        if n > 1:
            if not visited[n - 1]:
                visited[n - 1] = True
                queue.append((n - 1, cnt + 1))
        if n < b:
            if not visited[n + 1]:
                queue.append((n + 1, cnt + 1))
            if not visited[n * 2]:
                queue.append((n * 2, cnt + 1))

