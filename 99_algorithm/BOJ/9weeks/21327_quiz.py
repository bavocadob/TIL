# INF = int(1e9)
import sys
input = sys.stdin.readline

N, M, K, B = map(int, input().split())  # 문제수, 카테고리 수, 풀 수 있는 문제 수, 보너스 점수

categories = [list() for _ in range(M + 1)]

for _ in range(N):
    score, category = map(int, input().split())
    categories[category].append(score)

for i in range(1, M + 1):
    categories[i].sort(reverse=True)
    categories[i].insert(0, 0)
    for j in range(1, len(categories[i])):
        categories[i][j] = categories[i][j] + categories[i][j - 1]
        if j == len(categories[i]) - 1:
            categories[i][j] += B

# print(categories)
dp = [[0] * (K + 1) for _ in range(M + 1)]

for i in range(1, M + 1):  # i번 카테고리에서 선택
    for j in range(1, K + 1):  # K번 문제까지 선택할 수 있음
        for k in range(min(j + 1, len(categories[i]))):  # 해당 카테고리의 문제수 or j중 낮은 값
            temp_score = categories[i][k]
            # print(temp_score, str(i) + '번 카테고리', str(k) + '번 문제', str(j) + '번 문제까지 최대값')
            # print(dp[i - 1][j - k] + temp_score)
            dp[i][j] = max(dp[i][j], dp[i - 1][j], temp_score + dp[i - 1][j - k])
            # print(dp[i][j])

print(dp[M][K])
# print(dp)
