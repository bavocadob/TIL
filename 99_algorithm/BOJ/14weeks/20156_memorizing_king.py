import sys

input = sys.stdin.readline


def find(idx):
    if curr_parent[idx] == -1:
        return idx

    curr_parent[idx] = find(curr_parent[idx])
    return curr_parent[idx]


N, M, K = map(int, input().split())

parents = [-1] + list(map(int, input().split()))

curr_parent = [-1 for i in range(N + 1)]

visited = [False] * (N + 1)

students = []

for i in range(M):
    student = int(input())
    students.append(student)
    if not visited[student]:
        visited[student] = True
    else:
        students[i] = -1

for i in range(1, N + 1):
    if parents[i] == -1:
        continue
    if not visited[i]:
        curr_parent[find(i)] = find(parents[i])

queries = []

ans = [None] * K
for i in range(K):
    a, b, c = map(int, input().split())
    queries.append((a, b, c, i))

queries.sort(reverse=True)
query_idx = M - 1

for a, b, c, i in queries:
    while query_idx >= a:
        target = students[query_idx]
        query_idx -= 1
        if target == -1:
            continue
        curr_parent[target] = parents[target]

    pb = find(b)
    pc = find(c)
    ans[i] = (pb == pc)

for a in ans:
    if a:
        print('Same Same;')
    else:
        print('No;')
