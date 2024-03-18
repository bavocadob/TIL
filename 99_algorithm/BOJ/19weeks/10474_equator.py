import sys

input = sys.stdin.readline

INF = int(1e9)
T = int(input())

for _ in range(T):
    N, *numbers = map(int, input().split())

    max_size, temp_max, temp_min, max_val, min_val = 0, 0, 0, 0, 0

    for i in range(N):
        max_size += numbers[i]
        temp_max = max(numbers[i], temp_max + numbers[i])
        temp_min = min(numbers[i], temp_min + numbers[i])
        min_val = min(min_val, temp_min)
        max_val = max(max_val, temp_max)
    print(max(max_val, max_size - min_val))
