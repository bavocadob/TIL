import sys
input = sys.stdin.readline

def dfs(idx):
    stack = [idx]
    first = {idx}
    second = {numbers[idx]}

    while stack:
        curr = stack.pop()
        next_idx = numbers[curr]
        if next_idx not in first:
            first.add(next_idx)
            second.add(numbers[next_idx])
            stack.append(next_idx)

    if first == second:
        for i in first:
            visited[i] = True


N = int(input())

numbers = [0] + [int(input()) for _ in range(N)]

visited = [0] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

print(sum(visited))
for i in range(N + 1):
    if visited[i]:
        print(i)
