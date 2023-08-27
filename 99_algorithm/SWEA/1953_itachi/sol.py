import sys
from collections import deque

sys.stdin = open('input.txt')


def valid(x, y):
    return 0 <= x < N and 0 <= y < M


def passable(x, y, k):
    # 상 : 1,2,4,7
    # 하 : 1,2,5,6
    # 좌 : 1,3,6,7
    # 우 : 1,3,4,5
    if k == 0:
        return tunnel[x][y] in [1, 2, 5, 6]
    elif k == 1:
        return tunnel[x][y] in [1, 2, 4, 7]
    elif k == 2:
        return tunnel[x][y] in [1, 3, 4, 5]
    else:
        return tunnel[x][y] in [1, 3, 6, 7]


def bfs(x, y, t):
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    queue = deque([(x, y)])
    queue2 = deque()
    while queue and t > 0:
        while queue:
            i, j = queue.popleft()
            for k in tunnel_dict[tunnel[i][j]]:
                ni, nj = i + dx[k], j + dy[k]
                if valid(ni, nj) and tunnel[ni][nj] > 0 and not visited[ni][nj] and passable(ni, nj, k):
                    visited[ni][nj] = True
                    queue2.append((ni, nj))
        if queue2:
            queue = queue2
            queue2 = deque()
        t -= 1

    result = 0
    for v in visited:
        # print(v)
        result += sum(v)

    return result


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 상하좌우 2. 상하 3. 좌우 4. 상우
# 5. 하우 6. 하좌 7. 상좌
tunnel_dict = {1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3], 4: [0, 3], 5: [1, 3], 6: [1, 2], 7: [0, 2]}

T = int(input())

for tc in range(T):
    N, M, r, c, time = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc + 1} {bfs(r, c, time - 1)}')
