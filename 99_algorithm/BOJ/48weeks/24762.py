import sys


def find(v, parent):
    if parent[v] != v:
        parent[v] = find(parent[v], parent)
    return parent[v]


def union(u, v, parent, size):
    px = find(u, parent)
    py = find(v, parent)
    if px != py:
        parent[px] = py
        size[py] += size[px]


def main():
    n, m = map(int, sys.stdin.readline().split())

    parent = list(range(n))
    size = [1] * n

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        union(u - 1, v - 1, parent, size)

    component_sizes = []
    visited = set()
    for v in range(n):
        root = find(v, parent)
        if root not in visited:
            visited.add(root)
            component_sizes.append(size[root])

    total_pairs = n * (n - 1) // 2
    connected_pairs = sum(sz * (sz - 1) // 2 for sz in component_sizes)

    print(f"{connected_pairs / total_pairs:.6f}")


if __name__ == '__main__':
    main()
