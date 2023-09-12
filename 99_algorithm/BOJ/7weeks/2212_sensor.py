N = int(input())
K = int(input())

sensors = list(set(map(int, input().split())))
sensors.sort()
gap = [0] * (len(sensors) - 1)

for i in range(1, len(sensors)):
    gap[i - 1] = sensors[i] - sensors[i - 1]
gap.sort()

print(sum(gap[:len(gap) - K + 1]))
