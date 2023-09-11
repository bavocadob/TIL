import sys

input = sys.stdin.readline

N, M = map(int, input().split())

prefix_sum = [0] * (M + 1)

birds = []

for _ in range(N):
    direction, nakigoe = input().split()
    temp = [0] * (M + 1)

    if direction == 'L':
        direction = -1
    else:
        direction = 1

    for i in range(1, M + 1):
        if nakigoe[i - 1] == '1':
            temp[i] += direction
            prefix_sum[i] += direction
        temp[i] += temp[i - 1]

    birds.append(temp)

for i in range(1, M + 1):
    prefix_sum[i] += prefix_sum[i - 1]

disturbance = float('inf')
bird_idx = float('inf')

# print(prefix_sum)
for bird in range(N):
    temp = 0

    for second in range(1, M + 1):
        # print(birds[bird], second, temp)
        temp = max(temp, abs(prefix_sum[second] - birds[bird][second]))

    if temp < disturbance:
        disturbance = temp
        bird_idx = bird

print(bird_idx + 1)
print(disturbance)

# print(prefix_sum)
# print(birds)
