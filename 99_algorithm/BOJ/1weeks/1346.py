# 1로 만들기
# 다이나믹 프로그래밍

dp = {1: 0, 2: 1}


def solution(number):
    if number in dp:
        return dp[number]

    result = 1 + min(solution(number // 3) + number % 3, solution(number // 2) + number % 2)
    dp[number] = result

    return result


n = int(input())

print(solution(n))
