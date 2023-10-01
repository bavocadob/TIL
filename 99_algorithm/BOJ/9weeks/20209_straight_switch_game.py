import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    visited = {tuple(cube)}

    queue = deque([(tuple(cube))])
    queue2 = deque()
    cnt = 0

    while queue:

        while queue:
            curr = list(queue.popleft())
            temp = curr[1]
            flag = True
            for i in range(2, N + 1):
                if curr[i] != temp:
                    flag = False
                    break

            if flag:
                return cnt

            for k in range(1, K + 1):
                temp_lst = curr[:]
                for conn in switch[k]:
                    temp_lst[conn] = (temp_lst[conn] + k) % 5

                temp_tuple = tuple(temp_lst)
                if temp_tuple not in visited:
                    visited.add(temp_tuple)
                    queue2.append(temp_tuple)

        queue = queue2
        queue2 = deque()
        cnt += 1

    return -1


N, K = map(int, input().split())

switch = [list() for _ in range(K + 1)]

cube = [0] + list(map(int, input().split()))

for i in range(K):
    _, *adj = map(int, input().split())
    switch[i + 1].extend(adj)

print(bfs())
