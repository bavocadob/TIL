import heapq

N = int(input())
adj = [list() for _ in range(N)]

parents = list(map(int, input().split()))
for i in range(len(parents)):
    adj[parents[i] - 1].append(i + 1)

values = list(map(int, input().split()))

queue = [(-values[0], 0)]
ans = 0
for _ in range(N):
    val, curr_node = heapq.heappop(queue)
    ans += -val

    for next_node in adj[curr_node]:
        heapq.heappush(queue, (-values[next_node], next_node))

    print(ans)
