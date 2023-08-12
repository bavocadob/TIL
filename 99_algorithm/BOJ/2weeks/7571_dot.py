import sys
input = sys.stdin.readline

N, M = map(int, input().split())

x_arr = []
y_arr = []

for _ in range(M):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

x_arr.sort()
y_arr.sort()

x_pivot = x_arr[M // 2]
y_pivot = y_arr[M // 2]

result = 0

for i in range(M):
    result += abs(x_arr[i] - x_pivot)
    result += abs(y_arr[i] - y_pivot)


print(result)


