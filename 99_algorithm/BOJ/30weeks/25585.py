import sys

input = sys.stdin.readline
sys.setrecursionlimit(99999)

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]


def backtrack(x, y, depth, dist):
    global ans
    if dist >= ans:
        return

    if depth == region_cnt:
        ans = dist
        return

    for k in range(region_cnt):
        if visited[k]:
            continue
        nx, ny = regions[k]
        next_dist = max(abs(nx - x), abs(ny- y))

        visited[k] = True
        backtrack(nx, ny, depth + 1, dist + next_dist)
        visited[k] = False


def solve():
    global regions, ans
    target = (start_x + start_y) % 2

    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                if (i + j) % 2 != target:
                    print('Shorei')
                    return

    backtrack(start_x, start_y, 0, 0)
    if ans != INF:
        print('Undertaker')
        print(ans)


INF = int(1e9)
N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

start_x, start_y = -1, -1
visited = [[False] * N for _ in range(N)]
regions = []
region_cnt = 0

for i in range(N):
    flag = False
    for j in range(N):
        if A[i][j] == 2:
            start_x, start_y = i, j
        elif A[i][j] == 1:
            regions.append((i, j))
            region_cnt += 1

visited = [False] * region_cnt
ans = INF

solve()
