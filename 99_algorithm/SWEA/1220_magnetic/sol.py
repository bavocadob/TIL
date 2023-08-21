import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())

    fields = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        n = False
        for j in range(N):
            if fields[j][i] == 1:
                n = True
            elif fields[j][i] == 2:
                if n:
                    cnt += 1
                n = False

    print(f'#{tc} {cnt}')
