import sys
input = sys.stdin.readline

N, M = map(int, input().split())

connection = [set() for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    connection[x].add(y)
    connection[y].add(x)

visited = [False] * (N + 1)

min_friends = float('inf')

for i in range(1, N + 1):
    if len(connection[i]) < 2:
        continue

    for c in connection[i]:
        if connection[c] & connection[i]:
            third = connection[c] & connection[i]
            min_third = 9999
            for cc in third:
                min_third = min(min_third, len(connection[cc]))

            min_friends = min((len(connection[i]) - 2) + (len(connection[c]) - 2) + (min_third - 2), min_friends)


if min_friends != float('inf'):
    print(min_friends)
else:
    print(-1)