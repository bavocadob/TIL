N, M = map(int, input().split())

x, y = map(int, input().split())

time = int(input())

# time %= (N * M)

x_index = x + (time % (N * 2))

if x_index > N:
    x_index = abs(N * 2 - x_index)


# if x_index >= N * 2:
#     x_index = x_index % N
# elif x_index > N:
#     x_index = N - (x_index % N)

y_index = y + (time % (M * 2))

if y_index > M:
    y_index = abs(M * 2 - y_index)

# if y_index >= M * 2:
#     y_index = y_index % M
# elif y_index > M:
#     y_index = M - (y_index % M)

print(x_index, y_index)
