import sys

input = sys.stdin.readline

n, q = map(int, input().split())

cleared_rows = 0
cleared_cols = 0

sum_cleared_rows = 0
sum_cleared_cols = 0

base_sum = n * (n + 1) // 2

row_cleared = [False] * (n + 1)
col_cleared = [False] * (n + 1)

for _ in range(q):
    query_type, idx_str = input().split()
    idx = int(idx_str)

    if query_type == 'R':
        if row_cleared[idx]:
            print(0)
        else:
            result = (n - cleared_cols) * idx + (base_sum - sum_cleared_cols)
            print(result)
            row_cleared[idx] = True
            cleared_rows += 1
            sum_cleared_rows += idx
    else:
        if col_cleared[idx]:
            print(0)
        else:
            result = (n - cleared_rows) * idx + (base_sum - sum_cleared_rows)
            print(result)
            col_cleared[idx] = True
            cleared_cols += 1
            sum_cleared_cols += idx
