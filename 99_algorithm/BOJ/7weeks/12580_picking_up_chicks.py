import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    # 병아리 수, 헛간에 보내야 할 병아리 수, 헛간 위치, 시간
    N, K, B, T = map(int, input().split())

    # 첫째 줄 각 병아리의 초기 위치
    position = list(map(int, input().split()))
    # 둘째 줄 각 병아리의 속도
    speed = list(map(int, input().split()))

    chicken = 0
    loser = 0
    cnt = 0

    for i in range(N - 1, -1, -1):
        if position[i] + speed[i] * T >= B:
            chicken += 1
            cnt += loser
        else:
            loser += 1

        if chicken == K:
            break

    if chicken < K:
        cnt = 'IMPOSSIBLE'

    print(f'Case #{tc + 1}: {cnt}')
