def check_available(L):
    c_idx = 0
    for j in range(0, N, L):
        left = j
        right = min(j + L - 1, N - 1)

        if consecutive[c_idx][0] >= right:
            continue

        while c_idx < len(consecutive) and consecutive[c_idx][1] <= left:
            c_idx += 1

        if c_idx == len(consecutive):
            break

        while c_idx < len(consecutive) and consecutive[c_idx][0] < right and consecutive[c_idx][1] > left:
            if min(right, consecutive[c_idx][1]) - max(left, consecutive[c_idx][0]) + 1 >= K:
                return False
            c_idx += 1
        c_idx -= 1

        if c_idx >= len(consecutive):
            break

    return True


N, K = map(int, input().split())

novel = input() + ' '
curr_word = ''
curr_cnt = 0
curr_idx = 0

consecutive = []

for i in range(N + 1):
    if novel[i] == curr_word:
        curr_cnt += 1
    else:
        curr_word = novel[i]
        if curr_cnt >= K:
            consecutive.append((curr_idx, i - 1))
        curr_cnt = 1
        curr_idx = i

if not consecutive:
    print(N)
else:
    for i in range(N, K - 2, -1):
        if check_available(i):
            print(i)
            break
