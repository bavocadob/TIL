import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def solution(index, color):
    if dp[index][color] > 0:
        return dp[index][color]

    dp[index][color] = min(solution(index - 1, (color + 1) % 3) + costs[index][color],
                           solution(index - 1, (color + 2) % 3) + costs[index][color])

    return dp[index][color]


N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]

dp[0] = costs[0][:]

solution(N - 1, 0)
solution(N - 1, 1)
solution(N - 1, 2)

print(min(dp[N - 1]))