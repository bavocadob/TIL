N = int(input())

visited = [False] * (N + 1)

queue = []

for _ in range(N):
    reserve, arrive = map(int, input().split())
    if reserve == arrive:
        visited[reserve] = True
    else:
        queue.append((arrive, reserve))

queue.sort()

print(queue)
