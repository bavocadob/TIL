kkr_string = input()

r_cnt = kkr_string.count('R')

left = -1
right = len(kkr_string)

ans = r_cnt

if r_cnt == 0:
    print(0)
elif kkr_string.count('K') == 0:
    print(ans)
else:
    left_cnt = left_temp = 0
    right_cnt = right_temp = 0

    while left < right:
        if left_cnt <= right_cnt:
            left += 1
            if kkr_string[left] == 'K':
                left_cnt += 1
                if left > 0 and kkr_string[left - 1] == 'R':
                    r_cnt -= left_temp
                    left_temp = 0
            else:
                left_temp += 1
        else:
            right -= 1
            if kkr_string[right] == 'K':
                right_cnt += 1
                if right < len(kkr_string) - 1 and kkr_string[right + 1] == 'R':
                    r_cnt -= right_temp
                    right_temp = 0
            else:
                right_temp += 1

        if r_cnt == 0 or left == right:
            break
        ans = max(ans, min(left_cnt, right_cnt) * 2 + r_cnt)

    print(ans)
