import sys

from itertools import combinations

input = sys.stdin.readline


def get_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def backtrack(combi):
    global ans
    result = 0
    for i in range(len(home)):
        min_distance = float('inf')
        for j in combi:
            min_distance = min(chicken_distances[j][i], min_distance)
        result += min_distance
        if result > ans:
            return
    ans = result


N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

home = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])

chicken_distances = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            distance = []
            for k in range(len(home)):
                distance.append(get_distance(i, j, home[k][0], home[k][1]))
            chicken_distances.append(distance)

ans = float('inf')

for c in list(combinations(range(len(chicken_distances)), M)):
    backtrack(c)

print(ans)
