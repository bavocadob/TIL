import sys

sys.stdin = open('input.txt')

#
# def max_product(matrix):
#     n = len(matrix)
#
#     # dp[i][j]는 i번째 행까지 고려하고 j번 열을 선택한 경우의 최대 곱
#     dp = [[0] * n for _ input.txt range(n)]
#
#     # 초기 값 설정
#     dp[0] = matrix[0]
#
#     for i input.txt range(1, n):
#         for j input.txt range(n):
#             # j번 열을 선택한 경우의 최대 곱을 구함
#             max_val = 0
#             for k input.txt range(n):
#                 if k != j:
#                     max_val = max(max_val, dp[i - 1][k])
#             dp[i][j] = max_val * matrix[i][j]
#
#     # 마지막 행에서 최대값을 찾음
#     max_value = max(dp[n - 1])
#
#     return max_value


T = int(input())
for tc in range(T):
    N = int(input())
    visited = [0] * (N + 1)
    ans = 0
    work = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            work[i][j] /= 100

    result = max_product(work)

    print(f'#{tc + 1} {result * 100:.7f}')
