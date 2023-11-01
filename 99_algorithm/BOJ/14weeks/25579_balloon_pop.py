import sys

input = sys.stdin.readline


def find(idx):
    if parents[idx] == idx:
        return idx

    parents[idx] = find(parents[idx])
    return parents[idx]


def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return

    if px > py:
        px, py = py, px

    parents[py] = px
    sizes[px] += sizes[py]
    values[px] += values[py]


N = int(input())
parents = [i for i in range(N)]
sizes = [0 for _ in range(N)]

balloon_score = list(map(int, input().split()))
values = balloon_score[:]

orders = list(map(lambda x: int(x) - 1, input().split()))
ans = 0
temp = 0
for idx in range(len(orders) - 1, 0, -1):
    i = orders[idx]
    sizes[i] += 1

    if i - 1 >= 0 and sizes[find(i - 1)]:
        temp_left = find(i - 1)
        temp -= sizes[temp_left] * values[temp_left]
        union(i, i - 1)

    if i + 1 < N and sizes[find(i + 1)]:
        temp_right = find(i + 1)
        temp -= sizes[temp_right] * values[temp_right]
        union(i, i + 1)

    temp_parent = find(i)
    temp += sizes[temp_parent] * values[temp_parent]
    ans = max(temp, ans)

print(ans)
