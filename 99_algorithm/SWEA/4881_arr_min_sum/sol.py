import sys

sys.stdin = open('input.txt')


def solution(depth, val):
    global min_sum

    if depth == N:
        min_sum = min(min_sum, val)
        return
    if val > min_sum:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            solution(depth + 1, val + numbers[depth][i])
            visited[i] = False


for tc in range(1, int(input()) + 1):
    N = int(input())

    numbers = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 1000000
    visited = [False] * N

    solution(0, 0)
    print(f'#{tc} {min_sum}')
