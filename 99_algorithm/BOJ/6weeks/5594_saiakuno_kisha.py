import sys
input = sys.stdin.readline

from collections import deque


def bfs():
    queue = deque()

    for i in range(1, N + 1):
        if parent_cnt[i] == 0:
            queue.append(i)

    queue2 = deque()
    flag = False
    while queue:
        if len(queue) > 1:
            flag = True

        while queue:
            node = queue.popleft()
            print(node)
            for next_node in connection[node]:
                parent_cnt[next_node] -= 1

                if parent_cnt[next_node] == 0:
                    queue2.append(next_node)

        queue = queue2
        queue2 = deque()

    print(int(flag))


N = int(input())

M = int(input())

connection = [list() for _ in range(N + 1)]
parent_cnt = [0] * (N + 1)

for _ in range(M):
    win, lose = map(int, input().split())
    parent_cnt[lose] += 1
    connection[win].append(lose)

bfs()