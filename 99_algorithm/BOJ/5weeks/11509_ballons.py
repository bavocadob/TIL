from collections import defaultdict

arrows = defaultdict(int)

N = int(input())

balloons = list(map(int, input().split()))

for balloon in balloons:
    if arrows[balloon] > 0:
        arrows[balloon] -= 1
        arrows[balloon - 1] += 1
    else:
        arrows[balloon - 1] += 1

print(sum(arrows.values()))