V, E = map(int, input().split())


def find(idx):
    if parents[idx] == idx:
        return idx

    parents[idx] = find(parents[idx])
    return parents[idx]


def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        print('사이클')
        return
    if px < py:
        parents[py] = px
    else:
        parents[px] = py


edge = []

for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])

parents = [i for i in range(V)]

edge.sort(key=lambda x: x[2])

cnt = 0
sum_weight = 0
for f, t, w in edge:
    if find(f) != find(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        if cnt == V:
            break

print(sum_weight)
