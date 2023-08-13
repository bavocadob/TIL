# 수학문제인지 너비우선탐색 문제인지
# 첫 그리드는 1~50칸
# 상하좌우 하나씩 퍼뜨려나간다
# 최대 1500초가 주어지는데 50 * 50 을 꽉채운 상태에서 1500초동안 퍼뜨려 나간다고 가정하면 위 아래 옆으로 3000칸을 감
# 그럼 grid의 사이즈는 행 기준 N + (걸리는 초 * 2)만큼 만들면 된다.
# 너비 우선탐색으로 퍼뜨린 후 그 갯수를 print하면 됨
# 큐를 2개만들어서 한 큐가 소진되면 하루가 지날 수 있도록 설계
# 근데 pypy로는 통과가 되는데 python으로는 통과가 안됨.


from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

inner_grid = [input() for _ in range(N)]

days = int(input())
cnt = 0
queue1 = deque()
queue2 = deque()

row_size = days * 2 + N
col_size = days * 2 + M
grid = [[0] * col_size for _ in range(row_size)]

for i in range(N):
    for j in range(M):
        if inner_grid[i][j] == 'o':
            grid[i + days][j + days] = 1
            cnt += 1
            queue1.append((days + i, days + j))

curr_days = 0
while curr_days < days:
    while queue1:
        x, y = queue1.pop()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < row_size and 0 <= ny < col_size and grid[nx][ny] == 0:
                cnt += 1
                grid[nx][ny] = 1
                queue2.append((nx, ny))
    queue1 = queue2
    queue2 = deque()
    curr_days += 1

print(cnt)
