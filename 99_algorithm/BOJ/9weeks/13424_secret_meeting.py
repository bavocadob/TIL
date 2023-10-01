import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = int(1e9)


def solution():
    distances = [[INF] * K for _ in range(N + 1)]

    for i in range(K):
        distances[friends[i]][i] = 0
        queue = [(0, friends[i])]

        while queue:
            curr_dist, curr_room = heapq.heappop(queue)
            if distances[curr_room][i] < curr_dist:
                continue

            for next_room, weight in adj[curr_room].items():
                if distances[next_room][i] > (distance := curr_dist + weight):
                    distances[next_room][i] = distance
                    heapq.heappush(queue, (distance, next_room))

    min_dist = INF
    ans = 0

    for i in range(1, N + 1):
        temp_dist = sum(distances[i])
        if min_dist > temp_dist:
            ans = i
            min_dist = temp_dist

    return ans


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    adj = defaultdict(dict)

    for _ in range(M):
        v, e, p = map(int, input().split())
        adj[v][e] = p
        adj[e][v] = p

    K = int(input())

    friends = list(map(int, input().split()))
    print(solution())
