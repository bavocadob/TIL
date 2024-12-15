import sys

input = sys.stdin.readline
MOD = 1_000_000_007
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
A = [list(input().strip()) for _ in range(N)]


def power_of_two(num):
    if num == 1:
        return 2
    if num % 2:
        tmp = power_of_two(num - 1)
        return (2 * tmp) % MOD
    else:
        tmp = power_of_two(num // 2)
        return (tmp * tmp) % MOD


cnt = 0
for i in range(N):
    for j in range(M):
        flag = True
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if A[i][j] != A[nx][ny]:
                break
        else:
            cnt += 1

print(power_of_two(cnt))
