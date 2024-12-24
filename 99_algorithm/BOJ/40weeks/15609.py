import sys

input = sys.stdin.readline

N = int(input())
scores = [int(input()) for _ in range(N)]

sorted_scores = sorted(scores[1:], reverse=True) + [scores[0]]

tree_size = 1
while tree_size < N:
    tree_size *= 2

tree = [[] for _ in range(2 * N)]

for idx in range(N):
    tree_idx = tree_size + idx if tree_size + idx < 2 * N else tree_size - N + idx
    tree[tree_idx].append((idx, 1.0))

for node in range(N - 1, 0, -1):
    current = tree[node]
    for (left, right) in [(2 * node, 2 * node + 1), (2 * node + 1, 2 * node)]:
        for (i, prob_i) in tree[left]:
            total_prob = 0
            for (j, prob_j) in tree[right]:
                total_prob += prob_j * sorted_scores[i] / (sorted_scores[i] + sorted_scores[j])
            current.append((i, prob_i * total_prob))

for (idx, final_prob) in tree[1]:
    if idx == N - 1:
        print(f"{final_prob:.12f}")
