import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    files = list(map(int, input().split()))

    dp = [[0] * N for _ in range(N)]

    for right in range(1, N):
        for left in range(right - 1, -1, -1):
            temp = float('inf')

            # 제일 낮은값 찾기
            for k in range(right - left):
                temp = min(temp, dp[left][left + k] + dp[left + k + 1][right])

            dp[left][right] = temp + sum(files[left:right + 1])

            # left~right 값 더하기
            # for i input.txt range(left, right + 1):
            #     dp[left][right] += files[i]

    print(dp[0][N - 1])

    for d in dp:
        print(d)

    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

# F(ABCDE)
#
# F A~A + B~E
# F A~B + C~E
# F A~C + D~E
# F A~D + E~E
#
# i = 0이고 j = 4일때
# dp[0][4] =
# dp[0][0] + dp[1][4]
# dp[0][1] + dp[2][4]
# dp[0][2] + dp[3][4]
# dp[0][3] + dp[4][4]
#
# dp[1][4] =
# dp[1][1] + dp[2][4]
# dp[1][2] + dp[3][4]
# dp[1][3] + dp[4][4]
#
# dp[2][4] = (files[2] ~ files[4]) + min(
# dp[2][2] + dp[3][4]
# dp[2][3] + dp[4][4])

# dp[3][4] =
# dp[3][3] + dp[4][4]  + (files[3] ~ files[4])
