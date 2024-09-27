import math


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def can_reach(x1, y1, x2, y2):
    return R >= get_distance(x1, y1, x2, y2)


def get_maximum_customer():
    global ans

    temp = 0
    for x1, y1, men in solitairs:
        for x2, y2 in curr:
            if can_reach(x1, y1, x2, y2):
                temp += men
                break

    ans = max(ans, temp)


def dfs(depth, idx):
    if depth == K:
        get_maximum_customer()
        return

    for i in range(idx, M):
        if visited[i]:
            continue

        visited[i] = True
        curr.append(candidate[i])
        dfs(depth + 1, i + 1)
        visited[i] = False
        curr.pop()


ans = 0
K, R = map(int, input().split())
M = int(input())
candidate = [tuple(map(int, input().split())) for _ in range(M)]
N = int(input())
solitairs = [tuple(map(int, input().split())) for _ in range(N)]
visited = [False] * M
curr = []

dfs(0, 0)

print(ans)
