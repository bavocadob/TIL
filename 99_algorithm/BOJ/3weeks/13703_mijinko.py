# 미해결


def solution(height, time):
    if dp[height][time] != -1:
        return dp[height][time]

    if height == 0:
        return 0
    if height > time:
        return 2 ** time
    if time == 0:
        return 1

    dp[height][time] = solution(height + 1, time - 1) + solution(height - 1, time - 1)
    return dp[height][time]


dp = [[-1] * 200 for _ in range(100)]

centimeter, left_time = map(int, input().split())

print(solution(centimeter, left_time))
