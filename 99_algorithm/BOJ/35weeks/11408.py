import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

source = 1
sink = 2

MAX = N + M + 3
# source - 일들 -  직원 - sink

# 직원 -> sink 유량 = 1
# [N + 3][N + M + 3]

cost = [[0] * MAX for _ in range(MAX)]
capacity = [[0] * MAX for _ in range(MAX)]
adj = [list() for _ in range(MAX)]
flow = [[0] * MAX for _ in range(MAX)]

for i in range(3, M + 3):
    adj[source].append(i)
    adj[i].append(source)
    capacity[source][i] = 1

for i in range(M + 3, N + M + 3):  # i는 직원 번호
    temp = list(map(int, input().split()))
    capacity[i][sink] = 1
    adj[i].append(sink)
    adj[sink].append(i)

    work_length = temp[0]
    for j in range(work_length):
        work_idx, work_cost = temp[1 + (j * 2)], temp[j * 2 + 2]
        work_idx += 2
        adj[i].append(work_idx)
        adj[work_idx].append(i)
        capacity[work_idx][i] = 1
        cost[work_idx][i] = work_cost
        cost[i][work_idx] = -work_cost
ans = 0
ans_flow = 0
INF = int(1e9)

while True:
    is_in_queue = [False] * MAX
    parent = [0] * MAX
    dist = [INF] * MAX

    dist[source] = 0
    queue = deque([source])
    is_in_queue[source] = True

    while queue:
        # print(dist)
        cur = queue.popleft()

        is_in_queue[cur] = False
        for next_node in adj[cur]:  # 다음 노드가 유량이 더 흐를 수 있고, 거리상 비용이 더 저렴한 경우
            if capacity[cur][next_node] > flow[cur][next_node] and dist[next_node] > dist[cur] + cost[cur][next_node]:
                dist[next_node] = dist[cur] + cost[cur][next_node]
                parent[next_node] = cur
                if not is_in_queue[next_node]:
                    is_in_queue[next_node] = True
                    queue.append(next_node)

    if parent[sink] == 0:
        break

    idx = sink
    flow_value = INF

    while idx != source:
        flow_value = min(flow_value, capacity[parent[idx]][idx] - flow[parent[idx]][idx])
        idx = parent[idx]

    idx = sink
    ans_flow += flow_value
    while idx != source:
        ans += flow_value * cost[parent[idx]][idx]

        flow[parent[idx]][idx] += flow_value
        flow[idx][parent[idx]] -= flow_value
        idx = parent[idx]
print(ans_flow)
print(ans)
