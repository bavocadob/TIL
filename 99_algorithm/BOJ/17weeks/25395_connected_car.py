from collections import deque

N, S = map(int, input().split())

A = list(map(int, input().split()))
fuel = list(map(int, input().split()))

visited = [False] * N
visited[S - 1] = True
queue = deque([(S - 1, fuel[S - 1], A[S - 1])])

result = [S]

while queue:
    node, dist, position = queue.popleft()
    left = node - 1
    right = node + 1

    while left >= 0 and A[left] >= position - dist:
        if not visited[left]:
            queue.append((left, fuel[left], A[left]))
            result.append(left + 1)
            visited[left] = True
        left -= 1

    while right < N and A[right] <= position + dist:
        if not visited[right]:
            queue.append((right, fuel[right], A[right]))
            result.append(right + 1)
            visited[right] = True
        right += 1

result.sort()

print(*result)
