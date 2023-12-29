import sys

input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(p, c):
    p = find(p)
    c = find(c)
    if p == c:
        return

    parents[c] = p


N, A, B = map(int, input().split())

parents = [i for i in range(N + 1)]

post = [0] * (N + 1)

for _ in range(A):
    a, b = map(int, input().split())
    post[a] = b

for _ in range(B):
    a, b = map(int, input().split())
    post[a] = b
    union(a, b)

S = int(input())

for _ in range(S):
    e = int(input())
    target = find(e)

    if target == 0:
        print(-1)
        continue
    else:
        print(target)

    next_target = find(post[target])
    if next_target == target:
        next_target = post[target]

    parents[target] = next_target
    parents[next_target] = next_target
