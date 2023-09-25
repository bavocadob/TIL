import sys

input = sys.stdin.readline
sys.setrecursionlimit(999999)


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
        size[px] += size[py]
    else:
        parent[px] = py
        size[py] += size[px]


def add_dict(people, idx):
    if people not in people_dict:
        people_dict[people] = idx
        parent.append(idx)
        size.append(1)
        return 1
    return 0


T = int(input())
for tc in range(T):
    M = int(input())
    people_dict = dict()
    people_idx = 0
    parent = []
    size = []
    for _ in range(M):
        f1, f2 = input().split()
        people_idx += add_dict(f1, people_idx)
        people_idx += add_dict(f2, people_idx)
        union(people_dict[f1], people_dict[f2])
        print(size[find(people_dict[f1])])
