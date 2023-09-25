def calc_cnt(fuel):
    curr_pos = fuel
    charger_idx = 0
    c = 0
    # print('연료', fuel)
    # print(chargers)
    while curr_pos < distance and charger_idx <= N:
        # print(curr_pos, charger_idx)
        if chargers[charger_idx] > curr_pos:
            if curr_pos >= chargers[charger_idx - 1]:
                curr_pos = chargers[charger_idx - 1] + fuel
                c += 1
            else:
                break
        charger_idx += 1

    if curr_pos < distance:
        return - 1
    # print('결과', c, curr_pos)
    return c


distance, N, K = map(int, input().split())

chargers = list(map(int, input().split()))
chargers.append(distance)
left = 1
right = distance
result = distance
while left <= right:
    # print('왼족', left, '오른쪽', right)
    mid = (left + right) // 2

    cnt = calc_cnt(mid)

    if cnt <= K and cnt != -1:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
