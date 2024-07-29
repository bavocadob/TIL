S = input().rstrip()

temp = 0

str_len = []
coefficient = []

for i in range(len(S)):
    char = S[i]

    print(f'문자열 길이 {str_len}')
    print(f'계수 {coefficient}')

    if char.isdigit():
        temp += 1
    elif char == '(':
        str_len.append(temp - 1)
        coefficient.append(int(S[i - 1]))
        temp = 0
    else:
        level = coefficient.pop()
        value = temp * level
        temp = value + str_len.pop()

print(sum(str_len) + temp)
