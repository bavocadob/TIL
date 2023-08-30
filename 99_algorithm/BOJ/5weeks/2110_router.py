import sys

input = sys.stdin.readline

N, K = map(int, input().split())

house = [int(input()) for _ in range(N)]

house.sort()

left, right = 1, house[-1]


def calc(distance):
    cnt = 1

    curr = house[0]
    for i in range(1, N):
        if house[i] - curr >= distance:
            cnt += 1
            curr = house[i]

    return cnt


while left <= right:
    mid = (left + right) // 2
    # print(left, right)
    router = calc(mid)
    # 거리가 늘어나면 router가 줄어든다

    # 거리가 줄어들면 router가 늘어난다
    # 즉 router가 모자라면 거리를 줄여야 한다
    # router가 많으면 거리를 늘려야 한다
    # router가 같으면 거리를 조금 더 늘려봐도 된다
    if router >= K:
        left = mid + 1
    else:
        right = mid - 1
#외않되
print(left-1)
