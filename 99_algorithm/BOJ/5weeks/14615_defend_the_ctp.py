import sys

from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

connection = [list() for _ in range(N + 1)]
reverse_connection = [list() for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    connection[x].append(y)
    reverse_connection[y].append(x)

stack = [1]

visitable = defaultdict(bool)
visitable[1] = True
while stack:
    planet = stack.pop()

    for next_planet in connection[planet]:
        if not visitable[next_planet]:
            visitable[next_planet] = True
            stack.append(next_planet)

visitable_N = defaultdict(bool)

stack = [N]

while stack:
    planet = stack.pop()
    for next_planet in reverse_connection[planet]:
        if not visitable_N[next_planet]:
            visitable_N[next_planet] = True
            stack.append(next_planet)

C = int(input())

for _ in range(C):
    start = int(input())

    if visitable[start] and visitable_N[start]:
        print('Defend the CTP')
    else:
        print('Destroyed the CTP')
