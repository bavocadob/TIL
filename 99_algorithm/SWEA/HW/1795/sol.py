import sys

sys.stdin = open('input.txt')

from collections import defaultdict
import heapq

INF = int(1e9)


def dijkstra(adj_dict):
    hq = []
    distance = [INF] * (N + 1)
    distance[X] = 0
    heapq.heappush(hq, (0, X))

    while hq:
        # print(hq, '힙큐 상황')
        value, node = heapq.heappop(hq)
        # print(node, '현재 노드')
        if distance[node] < value:
            continue

        for next_node, weight in adj_dict[node]:
            if distance[next_node] <= value + weight:
                continue

            distance[next_node] = value + weight
            heapq.heappush(hq, (distance[next_node], next_node))

    return distance


T = int(input())

for tc in range(T):
    N, M, X = map(int, input().split())
    adj = defaultdict(list)
    adj_r = defaultdict(list)
    for _ in range(M):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))
        adj_r[e].append((s, w))

    insoo_to_friend = dijkstra(adj)
    # print(insoo_to_friend)
    friend_to_insoo = dijkstra(adj_r)
    # print(friend_to_insoo)
    ans = 0
    for i in range(1, N + 1):
        ans = max(insoo_to_friend[i] + friend_to_insoo[i], ans)

    print(f'#{tc + 1} {ans}')
