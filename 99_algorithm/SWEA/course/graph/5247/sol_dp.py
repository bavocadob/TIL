import sys

sys.stdin = open('input.txt')


def solution(target):
    if dp[target] != float('inf'):
        return dp[target]

    if not target % 2:
        dp[target] = min(dp[target], solution(target // 2))


T = int(input())

for tc in range(T):
    a, b = map(int, input().split())

    dp = [float('inf')] * (b * 2)
    dp[a] = 1
    print(solution(b))
