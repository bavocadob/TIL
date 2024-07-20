def solve(flag):
    dp = [[0] * 2 for _ in range(N + 1)]

    # 0은 해당 메인 통로에 개미가 살지 않음, 1은 해당 메인 통로에 개미가 살고 있다고 가정하기.
    if flag:  # 1번 통로에 개미 넣기
        dp[1][1] = 1

    dp[1][0] = A[0]

    for i in range(2, N):
        dp[i][1] = dp[i - 1][0] + 1
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0]) + A[i - 1]

    if flag:  # 1번 통로에 개미가 들어 있는 상태
        return max(dp[N - 1][0], dp[N - 1][1]) + A[N - 1]
    else:  # 1번 통로에 개미가 들어 있지 않는 상태
        return max(dp[N - 1][0] + 1, dp[N - 1][1] + A[N - 1])


N = int(input())

A = list(map(int, input().split()))

print(max(solve(True), solve(False)))
