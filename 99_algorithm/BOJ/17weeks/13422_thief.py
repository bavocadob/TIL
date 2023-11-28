import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())

    house = list(map(int, input().split()))
    if N > M:

        for i in range(M - 1):
            house.append(house[i])

        temp = 0

        for i in range(M):
            temp += house[i]

        ans = int(temp < K)

        for i in range(M, N + M - 1):
            temp += house[i] - house[i - M]
            if temp < K:
                ans += 1
    else:
        ans = int(sum(house) < K)

    print(ans)
