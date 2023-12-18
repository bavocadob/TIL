import sys

input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return False

    if px > py:
        px, py = py, px

    parents[py] = px
    return True


N = int(input())
parents = [i for i in range(N + 1)]
adj = []

lan_cable = 0

for i in range(1, N + 1):
    line = input().rstrip()

    for j, length in enumerate(line):
        if length == '0':
            continue

        if ord('A') <= ord(length) <= ord('Z'):
            size = ord(length) - ord('A') + 27
        else:
            size = ord(length) - ord('a') + 1
        adj.append((size, i, j + 1))

        lan_cable += size

adj.sort()

cost = 0
cnt = 1
for size, i, j in adj:
    if union(i, j):
        cost += size
        cnt += 1

if cnt == N:
    print(lan_cable - cost)
else:
    print(-1)
