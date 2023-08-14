N = int(input())

s = int(input())

input_str = input()


index = 0
cnt = 0
result = 0

while index < s - 2:

    if input_str[index] == 'I' and input_str[index + 1] == 'O' and input_str[index+2] == 'I':
        cnt += 1
        index += 2
    else:
        cnt = 0
        index += 1

    if cnt == N:
        result += 1
        cnt -= 1

print(result)
