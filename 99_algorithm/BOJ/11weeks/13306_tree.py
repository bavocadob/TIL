import sys

sys.setrecursionlimit(200001)

input = sys.stdin.readline


def find(idx):
    if parent[idx] == idx:
        return idx

    parent[idx] = find(parent[idx])
    return parent[idx]


N, Q = map(int, input().split())

parent_temp = [0, 1] + [int(input()) for _ in range(N - 1)]

queries = []

parent = [i for i in range(N + 1)]

for _ in range(N - 1 + Q):
    queries.append(tuple(map(int, input().split())))

result = []
for i in range(N + Q - 2, -1, -1):
    query = queries[i]
    if query[0]:  # 연결 여부 출력
        if find(query[1]) == find(query[2]):
            result.append('YES')
        else:
            result.append('NO')
    else:  # 유니온처리
        parent[query[1]] = parent_temp[query[1]]

print('\n'.join(result[::-1]))
