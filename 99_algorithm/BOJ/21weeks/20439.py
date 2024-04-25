import sys

input = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().split())

jobs = []

for _ in range(N):
    s, e = map(int, input().split())
    jobs.append((s, e))

jobs.append((1440, 1441))

# dp[i][j][b] = K개의 일들 중 i번째에 j번째 일을 선택했을 때 b 만큼의일이 선택된 상태에서 도달할 수 있는 가장 빠른 시간


new_jobs = list(map(int, input().split()))
dp = [[[INF] * (1 << K) for _ in range(K + 1)] for _ in range(K + 1)]

dp[0][0][0] = 0

for i in range(1, K + 1):
    for x in range(1, K + 1):
        # i - 1번째에 골랐었을 y 번째 일
        for y in range(K + 1):
            # 비트마스킹
            for b in range(1 << K):
                if 1 << (x - 1) & b or (y > 0 and (not 1 << (y - 1) & b)):
                    continue

                if dp[i - 1][y][b] == INF:
                    continue

                cost = new_jobs[x - 1]
                cur = dp[i - 1][y][b]
                for j in range(N + 1):
                    start, end = jobs[j]
                    if cur >= end:
                        continue

                    if cur + cost > start:
                        cur = end
                        if j == N - 1:
                            cur += cost
                    else:
                        cur += cost
                        break
                dp[i][x][b | 1 << (x - 1)] = cur

ans = INF

for i in range(1, K + 1):
    ans = min(ans, dp[K][i][(1 << K) - 1])


print('GOOD' if ans <= 1440 else 'BAD')
