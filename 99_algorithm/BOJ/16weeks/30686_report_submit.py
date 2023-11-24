import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

memorize = [0] + list(map(int, input().split()))

cases = list(permutations(range(M), M))

needs = []

for _ in range(M):
    _, *knowledge = map(int, input().split())
    needs.append(knowledge)

ans = int(1e9)

for case in cases:
    limit = [0] * (N + 1)
    temp = 0
    for today, homework in enumerate(case):
        for know in needs[homework]:
            if limit[know] <= today:
                temp += 1
                limit[know] = today + memorize[know]
    ans = min(temp, ans)

print(ans)
