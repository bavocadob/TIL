from itertools import combinations

n = int(input())
arr = []

for _ in range(n):
    f, c = map(int, input().split())
    arr.append((f, c))

m = int(input())
results = []

for _ in range(m):
    v, time = map(int, input().split())  # 비워내야 하는 물의 양, 제한 시간
    min_cost = float('inf')

    for r in range(1, n + 1):
        for gates in combinations(arr, r):
            total_flow = sum(g[0] * time for g in gates)
            total_cost = sum(g[1] for g in gates)
            if total_flow >= v:
                min_cost = min(min_cost, total_cost)

    if min_cost == float('inf'):
        results.append("Case {}: IMPOSSIBLE".format(_ + 1))
    else:
        results.append("Case {}: {}".format(_ + 1, min_cost))

for result in results:
    print(result)
