import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

adj = defaultdict(list)
par = defaultdict(int)
blood = defaultdict(float)
founder = input().rstrip()

blood[founder] = 1.0

for _ in range(N):
    baby, par_1, par_2 = input().split()
    par[baby] += 2
    par[par_1] = par[par_1]
    par[par_2] = par[par_2]

    adj[par_1].append(baby)
    adj[par_2].append(baby)

queue = []
for key, value in par.items():

    if not value:
        queue.append(key)

while queue:
    curr = queue.pop()
    for next_men in adj[curr]:
        par[next_men] -= 1
        blood[next_men] += blood[curr]
        if not par[next_men]:
            blood[next_men] /= 2
            queue.append(next_men)

max_blood = 0
next_king = None

for _ in range(M):
    candidate = input().rstrip()
    if blood[candidate] > max_blood:
        # region Description
        max_blood = blood[candidate]
        # endregion
        next_king = candidate

print(next_king)
