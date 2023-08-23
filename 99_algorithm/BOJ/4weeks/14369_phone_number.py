alphabet_dict = {0: [25, 4, 17, 14], 1: [14, 13, 4], 2: [19, 22, 14], 3: [19, 7, 17, 4, 4], 4: [5, 14, 20, 17],
                 5: [5, 8, 21, 4], 6: [18, 8, 23], 7: [18, 4, 21, 4, 13], 8: [4, 8, 6, 7, 19], 9: [13, 8, 13, 4]}

T = int(input())

for tc in range(T):
    phone_str = input()

    alphabet_cnt = [0] * 26

    for char in phone_str:
        alphabet_cnt[ord(char) - ord('A')] += 1
    # print(alphabet_cnt)
    result = []
    for i in range(0, 10, 2):
        min_val = 999999
        for a in alphabet_dict[i]:
            min_val = min(alphabet_cnt[a], min_val)
            # print(i, min_val)
        if min_val > 0:
            for a in alphabet_dict[i]:
                alphabet_cnt[a] -= min_val
            result.extend([str(i)] * min_val)

    for i in range(1, 10, 2):
        min_val = 999999
        for a in alphabet_dict[i]:
            min_val = min(alphabet_cnt[a], min_val)
        if min_val > 0:
            for a in alphabet_dict[i]:
                alphabet_cnt[a] -= min_val
            result.extend([str(i)] * min_val)
    result.sort()
    print(f'Case #{tc + 1}: {"".join(result)}')
