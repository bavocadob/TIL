import sys

sys.stdin = open('input.txt')


def find(idx):
    if parent[idx] == idx:
        return idx

    parent[idx] = find(parent[idx])
    return parent[idx]


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    if px < py:
        parent[py] = px
    else:
        parent[px] = py


T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]

    form = list(map(int, input().split()))

    for i in range(0, M * 2, 2):
        a, b = form[i], form[i + 1]
        union(a, b)

    s = set()
    for i in range(1, N + 1):
        s.add(find(i))

    print(f'#{tc + 1} {len(s)}')
