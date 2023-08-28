import sys

from collections import deque


def rotate(idx, d):
    left = gears[idx][6]
    right = gears[idx][2]
    # print(idx, d)
    # 오른쪽 기어를 회전시킬 수 있는지 판단
    if idx < 3:
        # 오른쪽의 기어를 방문하지 않았고, 오른쪽 기어의 왼쪽 맞닿는 면이 오른쪽 면과 다를 경우
        if not visited[idx + 1] and gears[idx + 1][6] != right:
            # 방문 처리를 한 후 반대 방향으로 회전
            visited[idx + 1] = True
            rotate(idx + 1, d * -1)

    # 왼쪽 기어를 회전시킬 수 있는지 판단
    if idx > 0:
        # 왼쪽 기어를 방문하지 않았고, 왼쪽 기어의 오른쪽 맞닿는 면이 왼쪽 면과 다를 경우
        if not visited[idx - 1] and gears[idx - 1][2] != left:
            # 방문 처리를 한 후 반대 방향으로 회전
            visited[idx - 1] = True
            rotate(idx - 1, d * -1)

    # 회전처리
    # 1은 시계방향 끝이 앞으로 옴
    # -1은 반시계방향 맨앞이 끝으로감
    if d == 1:
        gears[idx].appendleft(gears[idx].pop())
    else:
        gears[idx].append(gears[idx].popleft())


sys.stdin = open('input.txt')

T = int(input())

# 0 0 1 0 0 1 0 0
# 0번 인덱스 빨간 부분
# 2번 인덱스 오른쪽 맞닿는 부분
# 6번 인덱스 왼쪽 맞닿는 부분

for tc in range(T):

    k = int(input())
    gears = []

    for _ in range(4):
        gears.append(deque(list(map(int, input().split()))))

    # 회전 k번 시키기
    for _ in range(k):
        target, direction = map(int, input().split())
        visited = [False] * 4
        visited[target - 1] = True
        rotate(target - 1, direction)

    result = 0
    # 회전이 끝난 후 점수 합산
    for i in range(4):
        if gears[i][0]:
            result += 2 ** i

    print(f'#{tc + 1} {result}')
