N = int(input())
A = list(map(int, input().split()))

A.sort()

total_sum = 0
total_square_sum = 0
for val in A:
    total_sum += val
    total_square_sum += val ** 2

max_val = float('inf')
best_value = -1

left_sum = 0
for k in range(1, N + 1):
    left_sum += A[k - 1]
    current_value = A[k - 1]
    temp = (k - 1) * current_value - (left_sum - current_value) + \
           (total_sum - left_sum) - (N - k) * current_value

    if max_val > temp:
        max_val = temp
        best_value = current_value

print(best_value, end=" ")

max_val = float('inf')
best_k = -1

for k in range(1, 10001):
    temp = total_square_sum - 2 * k * total_sum + N * k ** 2

    if max_val > temp:
        max_val = temp
        best_k = k

print(best_k)
