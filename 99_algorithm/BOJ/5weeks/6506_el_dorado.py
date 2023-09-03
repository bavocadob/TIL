while True:
    N, K = map(int, input().split())

    if N == 0 and K == 0:
        break

    numbers = list(map(int, input().split()))

    # dp[i][j]: 인덱스가 i인 요소까지 사용하여 길이가 j인 부분 수열의 개수
    dp = [[0] * (K + 1) for _ in range(N)]

    for i in range(N):
        dp[i][1] = 1  # 길이가 1인 부분 수열은 항상 1개

    for i in range(N):
        for j in range(2, K + 1):
            for m in range(i):
                if numbers[i] > numbers[m]:
                    dp[i][j] += dp[m][j - 1]

    count = sum(dp[i][K] for i in range(N))
    print(dp)
    print(count)
