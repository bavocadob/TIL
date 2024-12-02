import math


def find_cycle_length(start, visited):
    length = 0
    current = start
    while not visited[current]:
        visited[current] = True
        current = perm[current]
        length += 1
    return length


def solve():
    visited = [False] * (N + 1)
    cycle_lengths = []

    for i in range(1, N + 1):
        if not visited[i]:
            cycle_lengths.append(find_cycle_length(i, visited))

    return math.lcm(*cycle_lengths)


N = int(input())
perm = [0] + list(map(int, input().split()))

print(solve())
