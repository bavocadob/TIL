import sys

input = sys.stdin.readline

INF = 987654321

while True:

    input_str = input().rstrip()

    if input_str == '0':
        break
    N, dice_range, turn = list(map(int, input_str.split()))

    board = []
    # 보드의 입력이 여러줄로 주어지고 예측이 안되므로 동적으로 보드 초기화
    while len(board) < N:
        board += list(map(int, input().split()))

    # print(board)

    dp = [[-INF] * N for _ in range(turn - 1)]
    # dp[0][0] = 0

    for i in range(dice_range):
        dp[0][i] = board[i]

    for t in range(1, turn - 1):
        for i in range(1, dice_range + 1):
            for j in range(i, N):
                if dp[t - 1][j - i] != -INF:
                    dp[t][j] = max(dp[t - 1][j - i] + board[j], dp[t][j])

    result = -INF
    for i in range(1, dice_range + 1):
        result = max(result, dp[-1][-i])

    print(result)

