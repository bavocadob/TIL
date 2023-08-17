N = int(input())

pillars = [list(map(int, input().split())) for _ in range(N)]

pillars.sort()

stack = [[0, 0]]

highest_pillar = 0

for i in range(N):
    highest_pillar = max(highest_pillar, pillars[i][1])

max_height = 0

for pillar in pillars:
    if pillar[1] >= stack[-1][1]:
        while max_height == highest_pillar and stack[-1][1] < pillar[1]:
            stack.pop()
        stack.append(pillar)
    else:
        if max_height == highest_pillar:
            stack.append(pillar)

    max_height = max(max_height, pillar[1])

result = 0

for i in range(len(stack) - 1):
    result += (stack[i + 1][0] - stack[i][0]) * min(stack[i][1], stack[i + 1][1])

result += max_height

print(result)
