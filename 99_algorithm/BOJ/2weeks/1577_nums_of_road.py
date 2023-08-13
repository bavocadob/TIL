# 도로의 개수
# 공사중인 도로를 set에 기억시켜놓고 경우의 수를 더할 때 공사중이라 판단되면 더하지 않기
# 세준이는 최소 경로로만 가려고 하므로 2가지 방향만 탐색하면서 오면 된다.

dx = [0, -1]
dy = [-1, 0]

N, M = map(int, input().split())

K = int(input())

city = [[0] * (M + 1) for _ in range(N + 1)]
city[0][0] = 1

construction = set()
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    construction.add((x1, y1, x2, y2))

for i in range(N + 1):
    for j in range(M + 1):
        for k in range(2):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni and 0 <= nj:
                if (i, j, ni, nj) not in construction and (ni, nj, i, j) not in construction:
                    city[i][j] += city[ni][nj]

print(city[N][M])