def compare(a, b):
    left = 0
    for k in range(3):
        if position[a][k] < position[b][k]:
            left += 1

    return left < 2


def solve():
    for i in range(N - 1):
        if compare(A[0][i], A[0][i + 1]):
            A[0][i], A[0][i + 1] = A[0][i + 1], A[0][i]


N = int(input())

position = [[] for _ in range(N + 1)]

A = []

for _ in range(3):
    A.append(list(map(int, input().split())))

for i in range(3):
    for j in range(N):
        position[A[i][j]].append(j)

solve()
print(*A[0])
