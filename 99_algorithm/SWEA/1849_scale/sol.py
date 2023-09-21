import sys

sys.stdin = open('input.txt')


def find(idx):
    if idx == parent[idx]:
        return idx
    # if parent[idx] != find(parent[idx]):
    #     parent[idx] = find(parent[idx])
    #     weight[idx] = weight[idx] + weight[parent[idx]]

    weight[idx] += weight[parent[idx]]
    parent[idx] = find(parent[idx])

    return parent[idx]


def union(a, b, w):
    pa = find(a)
    pb = find(b)

    if pa == pb:
        return

    if rank[pa] == rank[pb]:
        rank[pa] += 1

    if rank[pa] > rank[pb]:
        parent[pb] = pa
        weight[pb] = weight[a] - weight[b] - w
    else:
        parent[pa] = pb
        weight[pa] = weight[b] - weight[a] + w


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]
    weight = [0] * (N + 1)
    rank = [0] * (N + 1)
    result = []
    # print(f'#{tc + 1} ', end='')
    for _ in range(M):
        C, *data = input().split()
        if C == '!':
            a, b, ww = map(int, data)
            union(a, b, ww)
        else:
            a, b = map(int, data)
            parent_a = find(a)
            parent_b = find(b)
            if parent_a != parent_b:
                result.append('UNKNOWN')
                # print('UNKNOWN ', end='')
            else:
                result.append(str(weight[a] - weight[b]))
                # print(str(weight[a] - weight[b]), end=' ')

    print(f'#{tc + 1} {" ".join(result)}')

    # print(result)
    print(parent, '부모')
    print(rank, '계급')
    print(weight, '부모랑 차이')
