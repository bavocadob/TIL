import sys

sys.stdin = open('input.txt')

from collections import deque

for tc in range(1, 11):
    N, start = map(int, input().split())
    connection = [set() for _ in range(101)]

    route = list(map(int, input().split()))

    for i in range(0, N, 2):
        connection[route[i]].add(route[i + 1])

    queue = deque([start])
    time = 1
    visited = [0] * 101
    queue2 = deque()

    while queue:

        while queue:
            curr = queue.popleft()
            # print(connection[curr])
            for next_node in connection[curr]:

                if not visited[next_node]:
                    visited[next_node] = time
                    queue2.append(next_node)

        queue = queue2
        queue2 = deque()
        time += 1

    max_visited = 0
    max_idx = 0
    for i in range(101):
        if visited[i] > max_visited:
            max_visited = visited[i]
            max_idx = i
        elif visited[i] == max_visited:
            max_idx = i

    print(f'#{tc} {max_idx}')
