alphabet_cnt = [0] * 26

N = int(input())

for _ in range(N):
    input_str = input()
    length = len(input_str)

    for i, char in enumerate(input_str):
        alphabet_cnt[ord(char) - ord('A')] += 10 ** (length - 1 - i)

alphabet_cnt.sort(reverse=True)
result = 0
for i in range(10):
    result += alphabet_cnt[i] * (9 - i)

print(result)