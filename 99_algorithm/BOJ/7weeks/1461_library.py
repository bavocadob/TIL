N, M = map(int, input().split())

location = list(map(int, input().split()))
location.append(0)
location.sort()

cnt = -max(abs(location[0]), abs(location[-1]))

left = 0
right = N
zero_idx = location.index(0)

while left != zero_idx or right != zero_idx:
    if abs(location[left]) > abs(location[right]):
        cnt += abs(location[left] * 2)
        left = min(left + M, zero_idx)
    else:
        cnt += location[right] * 2
        right = max(right - M, zero_idx)

print(cnt)
