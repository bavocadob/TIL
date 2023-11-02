import sys

MOD = 1000000007

print = sys.stdout.write
input = sys.stdin.readline

fibonacci = [1, 1]

for i in range(2, 1_000_001):
    fibonacci.append((fibonacci[i - 1] + fibonacci[i - 2]) % MOD)


def find(idx):
    if parents[idx] == idx:
        return idx

    root = idx
    while parents[root] != root:
        root = parents[root]

    while idx != root:
        temp = parents[idx]
        parents[idx] = root
        idx = temp

    return root


# queries = []

N = int(input())

Q = int(input())
queries = sys.stdin.readlines()
# for _ in range(Q):
#     l, r = map(int, input().split())
#     l -= 1
#     r -= 1
#     queries.append((l, r))

parents = [i for i in range(N + 2)]
ans = [0] * N

for query in reversed(queries):
    temp_input = query.split()
    l, r = int(temp_input[0]) - 1, int(temp_input[1]) - 1
    i = find(l)

    while True:
        if not ans[i]:
            ans[i] = fibonacci[i - l + 1]

        i = find(i) + 1
        if i <= r:
            parents[i - 1] = i
        else:
            break

print(' '.join(map(str, ans)))

