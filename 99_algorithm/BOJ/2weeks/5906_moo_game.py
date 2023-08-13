N = int(input())

dp = [3]

i = 1
maximum = 1_000_000_000

while True:
    dp.append(dp[i - 1] * 2 + (i + 3))

    if dp[i] > maximum:
        break
    i += 1

# print(dp)

current_index = 0
while dp[current_index] < N:
    current_index += 1
# print(current_index)

while current_index > 0:
    if dp[current_index - 1] < N <= dp[current_index - 1] + current_index + 3:
        # 여기선 프린트를 해야해
        current_index -= 1
        N -= dp[current_index]
        break
    elif N < dp[current_index - 1]:
        current_index -= 1
    else:
        # print(N)
        N -= dp[current_index - 1] + current_index + 3
        current_index -= 1

# print(N)
if N == 1:
    print('m')
else:
    print('o')