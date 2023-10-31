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

orders = list(reversed(list(map(lambda x: int(x) - 1, input().split()))))
ans = 0

for i in orders:
    sizes[i] += 1

    if i - 1 >= 0 and sizes[find(i - 1)]:
        union(i, i - 1)

    if i + 1 < N and sizes[find(i + 1)]:
        union(i, i + 1)

    ans = max(ans, sizes[find(i)] * values[find(i)])
    print(values)
    print(sizes)
    print(ans)


