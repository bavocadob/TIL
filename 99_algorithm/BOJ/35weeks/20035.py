N, M = map(int, input().split())

max_val = 0
max_idx_start = 0
max_idx_end = 0

A = list(map(int, input().split()))

for i in range(N):
    num = A[i]

    if num > max_val:
        max_idx_start = max_idx_end = i
        max_val = num
    elif num == max_val:
        max_idx_end = i

B = list(map(int, input().split()))

right_max_val = 0
right_max_idx = 0

for i in range(M):
    num = B[i]

    if num > right_max_val:
        right_max_val = num
        right_max_idx = i

left = sum(A) + max_val * (M - 1)

aa = B[0] * max_idx_start
bb = sum(B[:right_max_idx])
cc = right_max_val * (max_idx_end - max_idx_start + 1)
dd = sum(B[right_max_idx + 1:])
ee = (N - 1 - max_idx_end) * B[-1]


right = aa + bb + cc + dd + ee
print(left * int(1e9) + right)

# 55000000068
# 55000000068
