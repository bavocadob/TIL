import sys

sys.stdin = open('input.txt')

T = int(input())


def dfs(depth, val):
    global result

    if val >= K:
        if val == K:
            result += 1
        return

    if depth == N:
        return

    dfs(depth + 1, val + numbers[depth])
    dfs(depth + 1, val)


for tc in range(T):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = 0
    dfs(0, 0)
    print(f'#{tc + 1} {result}')
