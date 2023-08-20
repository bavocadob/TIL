import sys

input = sys.stdin.readline

N = int(input())

villages = [list(map(int, input().split())) for _ in range(N)]

min_friendship = int(1e9)

for i in range(N):
    first_min = second_min = int(1e9)

    for j in range(N):
        if i != j:
            friendship = abs(villages[i][0] - villages[j][0]) + abs(villages[i][1] - villages[j][1]) + abs(
                villages[i][2] - villages[j][2])
            if friendship < first_min:
                second_min = first_min
                first_min = friendship
            elif friendship < second_min:
                second_min = friendship

    min_friendship = min(min_friendship, first_min + second_min)

print(min_friendship)
