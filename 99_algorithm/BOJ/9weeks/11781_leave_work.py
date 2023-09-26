import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

INF = float('inf')


def dijkstra(start):
    distances = [INF] * (N + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        curr_time, curr_node = heapq.heappop(queue)

        if curr_time > distances[curr_node]:
            continue

        for next_node, weight in adj[curr_node].items():

            time = curr_time
            if tie_up[curr_node][next_node]:
                # print(curr_node, next_node, time)
                if time < S:
                    spend_before_leave = min(S - time, weight)
                    time += spend_before_leave
                    weight -= spend_before_leave

                if weight and S <= time < E:
                    leave_time = E - time
                    spend_in_leave = min(weight, leave_time / 2)
                    time += spend_in_leave * 2
                    weight -= spend_in_leave

                if weight and time >= E:
                    time += weight
            else:
                time += weight

            if time < distances[next_node]:
                distances[next_node] = time
                heapq.heappush(queue, (time, next_node))
    return max(distances[1:])


N, M, S, E = map(int, input().split())
adj = defaultdict(dict)
tie_up = defaultdict(dict)

for _ in range(M):
    a, b, l, t1, t2 = map(int, input().split())
    adj[a][b] = l
    adj[b][a] = l
    tie_up[a][b] = t1
    tie_up[b][a] = t2

max_distance = dijkstra(1)
if max_distance % 1 == 0:
    print(int(max_distance))
else:
    print(max_distance)
