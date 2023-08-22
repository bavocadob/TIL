import sys

sys.stdin = open('input.txt')


def solution(idx):
    if idx * 2 <= N:
        solution(idx * 2)
    print(tree[idx], end='')
    if idx * 2 + 1 <= N:
        solution(idx * 2 + 1)


for tc in range(1, 11):

    N = int(input())

    tree = [None] * (N + 1)
    result = ''
    for i in range(N):
        temp = input().split()
        tree[i + 1] = temp[1]
    print(f'#{tc} ', end='')
    solution(1)
    print()
