import sys
sys.setrecursionlimit(999999)

def solution(target_val, depth):

    if dp[depth][target_val] != -1:
        return dp[depth][target_val]

    temp = 0
    if target_val + numbers[depth] <= 20:
        temp += solution(target_val + numbers[depth], depth - 1)

    if target_val - numbers[depth] >= 0:
        temp += solution(target_val - numbers[depth], depth - 1)

    dp[depth][target_val] = temp
    return dp[depth][target_val]


N = int(input())

dp = [[-1] * 21 for _ in range(N - 1)]

dp[0] = [0] * 21

numbers = list(map(int, input().split()))
dp[0][numbers[0]] = 1

solution(numbers[N - 1], N - 2)

print(dp[N - 2][numbers[N - 1]])
# for d in dp:
#     print(d)


