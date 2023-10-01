import sys

sys.setrecursionlimit(999999)
input = sys.stdin.readline


def dfs(curr_node, parent):
    for next_node in adj[curr_node]:
        if next_node != parent:
            dfs(next_node, curr_node)
            sizes[curr_node] += sizes[next_node]
            costs[curr_node] += costs[next_node]
            costs[curr_node] += (values[curr_node] ^ values[next_node]) * sizes[next_node]


def solution(curr_node, parent, cost):
    # 현재 노드가 루트노드일 경우의 값
    dp[curr_node] = costs[curr_node] + cost + (values[curr_node] ^ values[parent]) * (N - sizes[curr_node])
    # print(cost)
    # costs[curr_node] == 루트가 1일때 기준으로 현재노드의 자식들이 만들어 내는 비용
    # (values[curr_node] ^ values[parent]) * (N - sizes[curr_node]) == 내 부모 노드가 자식노드였을 경우에 소모될 비용
    # cost == 내 부모노드가 자식노드일 경우 그것의 자식노드들이 만들어 냈을 비용

    for next_node in adj[curr_node]:
        if next_node != parent:
            solution(next_node, curr_node,
                     dp[curr_node] - (values[curr_node] ^ values[next_node]) * sizes[next_node] - costs[next_node])
            # 내 현재 비용에서  내 자식 노드가 만들어낼 비용들을 빼면 뒤집어진 트리로 내가 루트트리가되고(자식 노드의 서브트리이면서) 그 값이 계산됨


T = int(input())

for tc in range(T):
    N = int(input())
    values = [0] + list(map(int, input().split()))

    adj = [list() for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    sizes = [1] * (N + 1)
    costs = [0] * (N + 1)
    dfs(1, 0)  # 루트가 1일때 기준으로 누적 cost값들을 노드별로 구하고 서브트리 사이즈도 구함

    # print(sizes)
    # print(costs)

    dp = [0] * (N + 1)
    solution(1, 0, 0)
    print(*dp[1:])
