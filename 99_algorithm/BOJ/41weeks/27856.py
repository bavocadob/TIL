import sys

input = sys.stdin.readline


def get_rem(val, ind, vval):
    res = val
    for k in vval:
        res -= ind % k
    return res


N = int(input().strip())

nums = []
while len(nums) < N:
    line = input().strip()
    nums.extend(map(int, line.split()))

cur_ind = 1
k_cnt = 0
k_tot = 0
k_rem = 0
k_vals = []

for cur_val in nums:
    if cur_ind == 1:
        k_tot = k_rem = cur_val
    else:
        rem = get_rem(cur_val, cur_ind, k_vals)

        new_rem = rem // cur_ind
        while new_rem < k_rem:
            k_vals.append(cur_ind)
            k_cnt += 1
            k_rem -= 1

        if k_rem == 0:
            break

    cur_ind += 1

print(k_tot, *k_vals)
