# 망가진 키보드

# m <= 128


while True:
    n = int(input())
    if n == 0:
        break

    ascii_check = [0] * 128
    input_txt = input()

    left = right = 0

    alphabet_cnt = 0
    max_length = 0

    txt_length = len(input_txt)
    while left <= right < txt_length:

        while right < txt_length and (alphabet_cnt < n or ascii_check[ord(input_txt[right])] > 0):
            if alphabet_cnt < n and ascii_check[ord(input_txt[right])] == 0:
                alphabet_cnt += 1

            ascii_check[ord(input_txt[right])] += 1
            right += 1

        # 왜 right - left + 1이 아니냐면 right의 현재 좌표는 문자열에서 카운트를 안했기 때문에
        max_length = max(max_length, right - left)

        while alphabet_cnt == n:
            ascii_check[ord(input_txt[left])] -= 1
            if ascii_check[ord(input_txt[left])] == 0:
                alphabet_cnt -= 1
            left += 1

    print(max_length)