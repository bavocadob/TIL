import sys

input = sys.stdin.readline


def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def backtrack(curr_x, curr_y, curr_hp, cnt):
    global ans

    if get_dist(curr_x, curr_y, home[0], home[1]) <= curr_hp:
        ans = max(ans, cnt)

    if cnt == 10:
        return

    for idx in range(len(mc_milk)):
        if visited[idx]:
            continue

        nx, ny = mc_milk[idx]
        next_dist = get_dist(curr_x, curr_y, nx, ny)

        if curr_hp >= next_dist:
            visited[idx] = True
            backtrack(nx, ny, curr_hp - next_dist + H, cnt + 1)
            visited[idx] = False


N, M, H = map(int, input().split())

home = (-1, -1)

mc_milk = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            home = (i, j)
        elif line[j] == 2:
            mc_milk.append((i, j))

ans = 0
visited = [False] * len(mc_milk)

backtrack(home[0], home[1], M, 0)

print(ans)
