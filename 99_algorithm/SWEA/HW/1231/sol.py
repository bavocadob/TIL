import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):

    N = int(input())

    tree = [None] * (N + 1)
    result = ''
    for i in range(N):
        temp = input().split()
        tree[i + 1] = temp[1]

    visited = [False] * (N + 1)

    curr = 1
    while True:
        if curr * 2 <= N and not visited[curr * 2]:
            curr *= 2
            continue
        else:
            if not visited[curr]:
                visited[curr] = True
                result += tree[curr]

        if curr * 2 + 1 <= N and not visited[curr * 2 + 1]:
            curr = curr * 2 + 1
            continue

        if curr // 2 > 0:
            curr = curr // 2
        else:
            break
    print(f'#{tc} {result}')
