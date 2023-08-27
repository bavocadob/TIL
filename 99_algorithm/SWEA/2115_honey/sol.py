import sys

sys.stdin = open('input.txt')


def solution(arr, temp_arr, depth):
    global max_val
    if sum(temp_arr) > C:
        return

    if depth == M:
        max_val = max(max_val, sum([honey ** 2 for honey in temp_arr]))
        return

    temp_arr.append(arr[depth])
    solution(arr, temp_arr, depth + 1)
    temp_arr.pop()
    solution(arr, temp_arr, depth + 1)


T = int(input())

for tc in range(T):
    N, M, C = map(int, input().split())

    hive = [list(map(int, input().split())) for _ in range(N)]

    # 한 줄에 M개의 연속된 꿀을 선택할 수 있는 경우의 수가 (N - M + 1)개 있음
    dp = [[0] * (N - M + 1) for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            max_val = 0
            solution(hive[i][j:j + M], [], 0)
            dp[i][j] = max_val

    result = 0

    for i in range(N):
        for j in range(N - M + 1):
            for ii in range(N):
                for jj in range(N - M + 1):
                    if i == ii and abs((j + M - 1) - (jj + M - 1)) < M:
                        continue
                    else:
                        result = max(result, dp[i][j] + dp[ii][jj])

    print(f'#{tc + 1} {result}')
