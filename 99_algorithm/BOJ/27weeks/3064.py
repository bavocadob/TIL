import sys

input = sys.stdin.readline


def solve():
    N = int(input())

    board = [input().rstrip() for _ in range(N)]

    if N <= 2:
        return 0
    elif N == 3:
        if int(board[0][0]):
            return 1
        else:
            return 0

    ans = 0

    for i in range(N):
        ans += int(board[0][i])
        ans += int(board[i][0])
        ans += int(board[i][N - 1])
        ans += int(board[N - 1][i])

    ans //= 3

    ans -= int(board[0][0])
    ans -= int(board[0][N - 1])
    ans -= int(board[N - 1][0])
    ans -= int(board[N - 1][N - 1])

    ans += (N - 4) ** 2

    return ans


T = int(input())

for _ in range(T):
    print(solve())
