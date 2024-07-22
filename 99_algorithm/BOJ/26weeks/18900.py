N = int(input())

A = list(map(int, input().split()))

idx_list = [-1] * (N + 1)

for i in range(N):
    idx_list[A[i]] = i

status = 0
cur_idx = idx_list[1]
cnt = 1

for i in range(2, N + 1):
    temp_idx = idx_list[i]

    if status == 0:
        status = 1 if temp_idx > cur_idx else -1
    elif (status == 1 and temp_idx < cur_idx) or (status == -1 and temp_idx > cur_idx):
        status = 0
        cnt += 1

    cur_idx = temp_idx

print(cnt)
